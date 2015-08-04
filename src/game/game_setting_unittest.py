#!/python
import unittest

import config
import game_setting

class TestGameSetting(unittest.TestCase):
  def testGameSettingStartResourcePilesDict(self):
    game_setting_obj = game_setting.GameSetting()
    start_resources = game_setting_obj.GetStartResourcesPilesDict()
    expected_resources = config.START_RESOURCES_PILES
    self.assertEqual(start_resources, expected_resources)

if __name__ == '__main__':
  unittest.main()
