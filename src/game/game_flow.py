"""This module handles the game flow."""

from game import enter_building_handler
from game import feeder
from game import feeding_handler
from game import take_resource_action
from game import resource
from game import resource_picker
from game.buildings import building_factory

class GameState(object):
  PENDING_ADD_PLAYERS = 'State: Pending adding players'
  PENDING_SET_RESOURCE_GENERATORS = 'State: Pending setting resource generators'
  PENDING_START_GAME = 'State: Pending start game'
  PENDING_USER_ACTION = 'State: Pending user action'
  PENDING_USER_FEE = 'State: Pending user paying entry fee'
  PENDING_USER_DONE = 'State: Pending user done'
  PENDING_FEEDING = 'State: Pending feeding'
  PENDING_START_NEXT_ROUND = 'State: Pending start of next round'


class GameFlowError(Exception):
  pass


def CheckState(state):
  def CheckStateDecorator(function):
    # pylint: disable=W0212
    def FunctionWithStateCheck(self, *args, **kwargs):
      if self._state != state:
        raise GameFlowError('Game state %s != %s' % (self._state, state))
      return function(self, *args, **kwargs)
    return FunctionWithStateCheck
  return CheckStateDecorator


class GameFlow(object):
  def __init__(self, setting):
    self._setting = setting
    self._resource_pile = resource.CreateResourceFromDict(
        setting.GetStartResourcesPilesDict())
    self._players = list()
    self._public_buildings = dict()
    self._resource_generators = list()
    self._turn_index = None
    self._current_player_index = None
    self._enter_building_handler = None
    self._round_index = None
    self._feeding_handler = None
    self._state = GameState.PENDING_ADD_PLAYERS
    self._end_of_round = None

  def GetResourcePile(self):
    return self._resource_pile

  @CheckState(GameState.PENDING_ADD_PLAYERS)
  def SetPlayers(self, players):
    self._players = players
    self._state = GameState.PENDING_SET_RESOURCE_GENERATORS

  def GetPlayer(self, name):
    for player_foo in self._players:
      if player_foo.GetName() == name:
        return player_foo

  @CheckState(GameState.PENDING_START_GAME)
  def StartGame(self):
    self._StartingOffer()
    self._StartingBuildings()
    self._current_player_index = 0
    self._turn_index = 0
    self._round_index = 0
    self._GetEndOfRound()
    self._StartPlayerTurn()

  def _GetEndOfRound(self):
    self._end_of_round = self._setting.GetEndOfRound(self._round_index)

  def _SetGeneratorVisible(self):
    self._resource_generators[self._turn_index].SetVisible()

  def _StartPlayerTurn(self):
    self._SetGeneratorVisible()
    self._GenerateResource()
    self._state = GameState.PENDING_USER_ACTION

  def _StartingOffer(self):
    starting_offer_dict = self._setting.GetLongGameStartingOffer()
    starting_offer = resource.CreateResourceFromDict(starting_offer_dict)
    for player_foo in self._players:
      player_foo.AddResource(starting_offer)

  def _StartingBuildings(self):
    for building_name in self._setting.GetStartingBuildings():
      building_obj = building_factory.CreateBuildingByName(building_name)
      self._public_buildings[building_name] = building_obj

  def GetPublicBuildings(self):
    return self._public_buildings

  @CheckState(GameState.PENDING_SET_RESOURCE_GENERATORS)
  def SetResourceGenerators(self, res_gen_list):
    self._resource_generators = res_gen_list
    self._state = GameState.PENDING_START_GAME

  def _GenerateResource(self):
    self._resource_pile.Add(
        self._resource_generators[self._turn_index].GetResource())

  @CheckState(GameState.PENDING_USER_DONE)
  def NextTurn(self):
    self._turn_index = self._turn_index + 1
    if self._turn_index == self._setting.GetNumberOfTurns():
      self._StartEndOfRoundFlow()
    else:
      self._StartNextPlayerTurn()

  def _StartNextPlayerTurn(self):
    self._NextPlayer()
    self._StartPlayerTurn()

  @CheckState(GameState.PENDING_START_NEXT_ROUND)
  def NextRound(self):
    self._round_index = self._round_index + 1
    self._GetEndOfRound()
    self._turn_index = 0
    self._StartNextPlayerTurn()

  def _NextPlayer(self):
    self._current_player_index = self._current_player_index + 1
    if self._current_player_index == len(self._players):
      self._current_player_index = 0

  def _StartEndOfRoundFlow(self):
    self._CreateFeedHandler(self._end_of_round.food)
    self._state = GameState.PENDING_FEEDING

  def _CreateFeedHandler(self, food_req):
    self._feeding_handler = feeding_handler.FeedingHandler()
    for player_index in xrange(len(self._players)):
      player_obj = self._players[player_index]
      picker_obj = resource_picker.CreateResourcePickerForFood(
          player_obj.GetResource())
      feeder_obj = feeder.CreateFeeder(player_obj, food_req, picker_obj)
      self._feeding_handler.AddFeeder(player_obj.GetName(), feeder_obj)

  @CheckState(GameState.PENDING_FEEDING)
  def GetFeederForPlayer(self, name):
    return self._feeding_handler.GetFeeder(name)

  @CheckState(GameState.PENDING_FEEDING)
  def FeedWithPickedForPlayer(self, name):
    self._feeding_handler.FeedWithPicked(name)
    if self._feeding_handler.IsAllDone():
      self._state = GameState.PENDING_START_NEXT_ROUND

  def SetResourcePileForTest(self, res_pile):
    self._resource_pile = res_pile

  @CheckState(GameState.PENDING_USER_ACTION)
  def PlayerTakeResourceAction(self, res_name):
    player = self.GetCurrentPlayer()
    action = take_resource_action.CreateTakeResourceAction(res_name)
    action.TakeAction(player, self.GetResourcePile())
    self._state = GameState.PENDING_USER_DONE

  @CheckState(GameState.PENDING_USER_ACTION)
  def PlayerTakeDummyActionForTest(self):
    self._state = GameState.PENDING_USER_DONE

  @CheckState(GameState.PENDING_USER_ACTION)
  def PlayerEnterBuildingAction(self, building_key):
    player_obj = self.GetCurrentPlayer()
    building_obj = self._public_buildings[building_key]
    fee = building_obj.GetFee()
    picker_obj = resource_picker.CreateResourcePickerForEntryFee(
        player_obj.GetResource(), fee)
    self._enter_building_handler = enter_building_handler.EnterBuildingHandler(
        building_obj=building_obj,
        player_obj=player_obj,
        picker_obj=picker_obj,
        )

    self._state = GameState.PENDING_USER_FEE
    if fee.franc or fee.food:
      return
    else:
    # Pay nothing and enter this building.
      self.PayEntryFee()

  @CheckState(GameState.PENDING_USER_FEE)
  def GetEnterBuildingHandler(self):
    return self._enter_building_handler

  @CheckState(GameState.PENDING_USER_FEE)
  def PayEntryFee(self):
    self._enter_building_handler.EnterBuilding() 
    self._state = GameState.PENDING_USER_DONE

  def GetCurrentPlayer(self):
    return self._players[self._current_player_index]

  def GetCurrentTurn(self):
    return self._turn_index

  def GetCurrentRound(self):
    return self._round_index

  def GetResourceGenerators(self):
    return self._resource_generators

  def GetThisRoundFoodRequirement(self):
    return self._end_of_round.food

  def GetGameState(self):
    return self._state



def CreateGameFlow(setting):
  return GameFlow(setting)
