"""This module handles the game flow."""

import take_resource_action
import resource

class GameFlow(object):
  def __init__(self, setting):
    self._setting = setting
    self._resource_pile = resource.CreateResourceFromDict(
        setting.GetStartResourcesPilesDict())
    self._players = list()
    self._resource_generators = list()
    self._turn_index = 0
    self._current_player_index = 0

  def GetResourcePile(self):
    return self._resource_pile

  def AddPlayer(self, new_player):
    self._players.append(new_player)

  def GetPlayer(self, name):
    for player_foo in self._players:
      if player_foo.GetName() == name:
        return player_foo

  def StartingOffer(self):
    starting_offer_dict = self._setting.GetLongGameStartingOffer()
    starting_offer = resource.CreateResourceFromDict(starting_offer_dict)
    for player_foo in self._players:
      player_foo.AddResource(starting_offer)

  def SetResourceGenerators(self, res_gen_list):
    self._resource_generators = res_gen_list

  def GenerateResource(self):
    self._resource_pile.Add(
        self._resource_generators[self._turn_index].GetResource())

  def NextTurn(self):
    self._turn_index = self._turn_index + 1
    self._NextPlayer()

  def _NextPlayer(self):
    self._current_player_index = self._current_player_index + 1
    if self._current_player_index == len(self._players):
      self._current_player_index = 0

  def SetResourcePileForTest(self, res_pile):
    self._resource_pile = res_pile

  def PlayerTakeResourceAction(self, res_name):
    player = self.GetCurrentPlayer()
    action = take_resource_action.CreateTakeResourceAction(res_name)
    action.TakeAction(player, self.GetResourcePile())

  def GetCurrentPlayer(self):
    return self._players[self._current_player_index]

def CreateGameFlow(setting):
  return GameFlow(setting)
