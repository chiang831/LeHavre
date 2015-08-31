"""Interact console for testing."""
import code

import player
import game_setting
import game_flow
import resource_generator

import simple_resource_viewer
import simple_player_viewer
import simple_feeder_viewer

#TODO: Add unittest for this module.

class InteractShell(object):
  def __init__(self):
    self._flow = None
    self._names = None
    self._players = list()
    self._setting = None

  def RestartGame(self):
    self._CreatePlayers()
    self._CreateGameFlow()

  def _CreatePlayers(self):
    self._players = list()
    for name in self._names:
      player_obj = player.Player(name)
      self._players.append(player_obj)

  def StartGame(self, names):
    """Start a game with a list of player names."""
    self._names = names
    self._CreatePlayers()
    self._setting = game_setting.GameSetting(len(names))
    self._CreateGameFlow()

  def _AddPlayers(self):
    self._flow.SetPlayers(self._players)

  def _CreateGameFlow(self):
    self._flow = game_flow.GameFlow(self._setting)
    self._AddPlayers()
    self._flow.SetResourceGenerators(
        resource_generator.GetShuffledResourceGenerators())
    self._flow.StartGame()

  def ShowResourcePile(self):
    print simple_resource_viewer.ShowResource(self._flow.GetResourcePile())

  def ShowPlayers(self):
    for player_obj in self._players:
      print simple_player_viewer.ShowPlayer(player_obj)

  def PlayerTakeResourceAction(self, resource_name):
    self._flow.PlayerTakeResourceAction(resource_name)

  def PlayerDone(self):
    self._flow.NextTurn()

  def ShowFeeder(self, player_name):
    feeder = self._flow.GetFeederForPlayer(player_name)
    print simple_feeder_viewer.ShowFeeder(feeder)

  def GetPickerForPlayer(self, player_name):
    feeder = self._flow.GetFeederForPlayer(player_name)
    return feeder.GetResourcePicker()

  def PlayerFeedDone(self, player_name):
    self._flow.FeedWithPickedForPlayer(player_name)

  def NextRound(self):
    self._flow.NextRound()


# pylint: disable=C0103
p = InteractShell()
variables = globals().copy()
variables.update(locals())
shell = code.InteractiveConsole(variables)
shell.interact()
