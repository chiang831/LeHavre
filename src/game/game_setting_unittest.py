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

  def testGameSettingLongGameStartingOffer(self):
    game_setting_obj = game_setting.GameSetting()
    starting_offer = game_setting_obj.GetLongGameStartingOffer()
    expected_resources = config.LONG_GAME_STARTING_OFFER
    self.assertEqual(starting_offer, expected_resources)

if __name__ == '__main__':
  unittest.main()
