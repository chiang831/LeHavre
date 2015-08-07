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

  def _CreateAndAddPlayer(self, name):
    p = player.Player(name)
    self._flow.AddPlayer(p)
    return p

  def testGameFlowStartingResourcePile(self):
    expected_resource_pile = resource.CreateResourceFromDict(
        config.START_RESOURCES_PILES)
    self.assertTrue(
        self._flow.GetResourcePile().Equal(expected_resource_pile))

  def testGameFlowAddPlayer(self):
    name = 'Player1'
    self._CreateAndAddPlayer(name)
    self.assertEqual(name, self._flow.GetPlayer(name).GetName())

  def testGameStartingOffer(self):
    name1 = 'Player1'
    name2 = 'Player2'
    p1 = self._CreateAndAddPlayer(name1)
    p2 = self._CreateAndAddPlayer(name2)
    self._flow.StartingOffer()
    expected_resource = resource.CreateResourceFromDict(
        config.LONG_GAME_STARTING_OFFER)
    self.assertTrue(p1.GetResource().Equal(expected_resource))
    self.assertTrue(p2.GetResource().Equal(expected_resource))

if __name__ == '__main__':
  unittest.main()
