import unittest

import config
import game_flow
import game_setting
import resource

class TestGameFlow(unittest.TestCase):
  def setUp(self):
    setting = game_setting.GameSetting()
    self._flow = game_flow.CreateGameFlow(setting) 

  def testGameFlowStartingResourcePile(self):
    expected_resource_pile = resource.CreateResourceFromDict(
        config.START_RESOURCES_PILES)
    self.assertTrue(
        self._flow.GetResourcePile().Equal(expected_resource_pile))

if __name__ == '__main__':
  unittest.main()
