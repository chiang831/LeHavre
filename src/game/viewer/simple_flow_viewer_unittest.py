"""Unittest for simple_player_viewer."""

import unittest

from game import player
from game import game_flow
from game import game_setting
from game import resource_generator

from game.viewer import simple_flow_viewer

class TestFlowViewer(unittest.TestCase):
  def setUp(self):
    self._game_setting = None
    self._flow = None
    self._players = None
    self._generators = None

  def _CreateTestFlow(self):
    self._game_setting = game_setting.GameSetting(1)
    self._flow = game_flow.CreateGameFlow(self._game_setting)
    self._players = [player.Player('Player1')]
    self._flow.SetPlayers(self._players)
    self._generators = resource_generator.GetShuffledResourceGenerators()
    self._flow.SetResourceGenerators(self._generators)

  def testFlowViewer(self):
    self._CreateTestFlow()
    self._flow.StartGame()

    expected_output = ('Game State: %s\n' %
                       game_flow.GameState.PENDING_USER_ACTION)

    food = self._game_setting.GetEndOfRound(0).food
    expected_output += 'Round: 1    Turn: 1    Food Requirement: %d\n' % food

    expected_output += 'Current player: Player1\n'

    flow_viewer = simple_flow_viewer.SimpleFlowViewer(self._flow)
    self.assertEqual(expected_output, flow_viewer.Show())

    show_flow_output = simple_flow_viewer.ShowFlow(self._flow)
    self.assertEqual(expected_output, show_flow_output)


if __name__ == '__main__':
  unittest.main()
