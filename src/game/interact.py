"""Interact console for testing."""
import code
import readline
import rlcompleter

from game import player
from game import game_setting
from game import game_flow
from game import resource_generator

from game.viewer import simple_building_viewer
from game.viewer import simple_feeder_viewer
from game.viewer import simple_flow_viewer
from game.viewer import simple_player_viewer
from game.viewer import simple_resource_generator_viewer
from game.viewer import simple_resource_viewer

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
    print 'Resource piles:'
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

  def ShowFlow(self):
    flow_viewer = simple_flow_viewer.SimpleFlowViewer(self._flow)
    print flow_viewer.Show()

  def ShowGenerators(self):
    generator_viewer = simple_resource_generator_viewer.\
        SimpleResourceGeneratorsViewer(self._flow.GetResourceGenerators())
    print generator_viewer.Show()

  def ShowPublicBuildings(self):
    print 'Public buildings: \n'
    for name, building in self._flow.GetPublicBuildings().iteritems():
      print '[%s]: ' % name
      print simple_building_viewer.SimpleBuildingViewer(building).Show()

  def ShowAll(self):
    self.ShowFlow()
    self.ShowGenerators()
    self.ShowResourcePile()
    self.ShowPublicBuildings()
    self.ShowPlayers()


def Run():
  # pylint: disable=C0103
  p = InteractShell()
  p.StartGame(['Jimmy', 'Jennifer'])
  p.ShowAll()
  variables = globals().copy()
  variables.update(locals())
  readline.set_completer(rlcompleter.Completer(variables).complete)
  readline.parse_and_bind("tab: complete")
  shell = code.InteractiveConsole(variables)
  shell.interact()
