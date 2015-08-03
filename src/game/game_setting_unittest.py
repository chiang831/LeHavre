#!/python
import unittest
import game_setting
import game_start_config

class TestGameSetting(unittest.TestCase):
  def testGameSettingStart(self):
    game_setting = game_setting.GameSetting()
    start_resources = game_setting.GetStartResources()
    expected_resources = game.game_start_config.GAME_START_RESOURCES_PILES
    self.assertEqual(start_resources, expected_resources)
