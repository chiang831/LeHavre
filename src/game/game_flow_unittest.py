import unittest

import config
import game_flow
import game_setting
import resource

class TestGameFlow(unittest.TestCase):
  def testGameFlowStartingResourcePile(self):
    setting = game_setting.GameSetting()
    flow = game_flow.CreateGameFlow(setting) 
    expected_resource_pile = resource.CreateResourceFromDict(
        config.START_RESOURCES_PILES)
    self.assertTrue(
        flow.GetResourcePile().Equal(expected_resource_pile))

if __name__ == '__main__':
  unittest.main()
