import unittest

import config
import game_flow
import game_setting
import resource
import player

class TestGameFlow(unittest.TestCase):
  def setUp(self):
    setting = game_setting.GameSetting()
    self._flow = game_flow.CreateGameFlow(setting) 

  def testGameFlowStartingResourcePile(self):
    expected_resource_pile = resource.CreateResourceFromDict(
        config.START_RESOURCES_PILES)
    self.assertTrue(
        self._flow.GetResourcePile().Equal(expected_resource_pile))

  def testGameFlowAddPlayer(self):
    name = 'Player1'
    player1 = player.Player(name)
    self._flow.AddPlayer(player1)
    self.assertEqual(name, self._flow.GetPlayer(name).GetName())

if __name__ == '__main__':
  unittest.main()
