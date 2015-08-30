"""This module handles the game flow."""

import feeder
import feeding_handler
import take_resource_action
import resource
import resource_picker

class GameFlowError(Exception):
  pass

class GameFlow(object):
  def __init__(self, setting):
    self._setting = setting
    self._resource_pile = resource.CreateResourceFromDict(
        setting.GetStartResourcesPilesDict())
    self._players = list()
    self._resource_generators = list()
    self._turn_index = None
    self._current_player_index = None
    self._round_index = None
    self._feeding_handler = None
    self._pending_action = None
    self._pending_end_of_round = None

  def GetResourcePile(self):
    return self._resource_pile

  def AddPlayer(self, new_player):
    self._players.append(new_player)

  def GetPlayer(self, name):
    for player_foo in self._players:
      if player_foo.GetName() == name:
        return player_foo

  def StartGame(self):
    self._StartingOffer()
    self._current_player_index = 0
    self._turn_index = 0
    self._round_index = 0
    self._StartPlayerTurn()

  def _StartPlayerTurn(self):
    self._GenerateResource()
    self._pending_action = True

  def _StartingOffer(self):
    starting_offer_dict = self._setting.GetLongGameStartingOffer()
    starting_offer = resource.CreateResourceFromDict(starting_offer_dict)
    for player_foo in self._players:
      player_foo.AddResource(starting_offer)

  def SetResourceGenerators(self, res_gen_list):
    self._resource_generators = res_gen_list

  def _GenerateResource(self):
    self._resource_pile.Add(
        self._resource_generators[self._turn_index].GetResource())

  def NextTurn(self):
    if self._pending_end_of_round:
      raise GameFlowError('Pending end of round')

    if self._pending_action:
      raise GameFlowError('Player action not done yet')

    self._turn_index = self._turn_index + 1
    if self._turn_index == self._setting.GetNumberOfTurns():
      self._StartEndOfRoundFlow()
    else:
      self._StartNextPlayerTurn()

  def _StartNextPlayerTurn(self):
    self._NextPlayer()
    self._StartPlayerTurn()

  def NextRound(self):
    if not self._pending_end_of_round:
      raise GameFlowError('Not in end of round')
    if self._EndOfRoundFlowDone():
      self._round_index = self._round_index + 1
      self._turn_index = 0
      self._pending_end_of_round = False
      self._StartNextPlayerTurn()
    else:
      raise GameFlowError('Feeding is not done yet')

  def _NextPlayer(self):
    self._current_player_index = self._current_player_index + 1
    if self._current_player_index == len(self._players):
      self._current_player_index = 0

  def _StartEndOfRoundFlow(self):
    end_of_round = self._setting.GetEndOfRound(self._round_index)
    self._CreateFeedHandler(end_of_round.food)
    self._pending_end_of_round = True

  def _EndOfRoundFlowDone(self):
    return self._feeding_handler.IsAllDone()

  def _CreateFeedHandler(self, food_req):
    self._feeding_handler = feeding_handler.FeedingHandler()
    for player_index in xrange(len(self._players)):
      player_obj = self._players[player_index]
      picker_obj = resource_picker.CreateResourcePickerForFood(
          player_obj.GetResource())
      feeder_obj = feeder.CreateFeeder(player_obj, food_req, picker_obj)
      self._feeding_handler.AddFeeder(player_obj.GetName(), feeder_obj)

  def GetFeederForPlayer(self, name):
    return self._feeding_handler.GetFeeder(name)

  def FeedWithPickedForPlayer(self, name):
    self._feeding_handler.FeedWithPicked(name)

  def SetResourcePileForTest(self, res_pile):
    self._resource_pile = res_pile

  def PlayerTakeResourceAction(self, res_name):
    if not self._pending_action:
      raise GameFlowError('Player has done the action')
    player = self.GetCurrentPlayer()
    action = take_resource_action.CreateTakeResourceAction(res_name)
    action.TakeAction(player, self.GetResourcePile())
    self._pending_action = False

  def PlayerTakeDummyActionForTest(self):
    if not self._pending_action:
      raise GameFlowError('Player has done the action')
    self._pending_action = False

  def GetCurrentPlayer(self):
    return self._players[self._current_player_index]

def CreateGameFlow(setting):
  return GameFlow(setting)
