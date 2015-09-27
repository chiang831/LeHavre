"""Unittest for game_setting module."""

import unittest

from game import config
from game import game_setting

class TestGameSetting(unittest.TestCase):
  def setUp(self):
    self._number_of_players = 1
    self._game_setting_obj = None

  def testGameSettingStartResourcePilesDict(self):
    self._CreateGameSettingObject()
    start_resources = self._game_setting_obj.GetStartResourcesPilesDict()
    expected_resources = config.START_RESOURCES_PILES
    self.assertEqual(start_resources, expected_resources)

  def testGameSettingLongGameStartingOffer(self):
    self._CreateGameSettingObject()
    starting_offer = self._game_setting_obj.GetLongGameStartingOffer()
    expected_resources = config.LONG_GAME_STARTING_OFFER
    self.assertEqual(starting_offer, expected_resources)

  def _TestEndOfRound(self):
    self._CreateGameSettingObject()
    number_of_rounds = len(config.END_OF_ROUND_DICT[self._number_of_players])
    for round_index in xrange(number_of_rounds):
      self._TestEndOfRoundOneRound(round_index)

  def _TestEndOfRoundOneRound(self, round_index):
    round_ending_obj = self._game_setting_obj.GetEndOfRound(round_index)
    self.assertEqual(
        round_ending_obj,
        config.END_OF_ROUND_DICT[self._number_of_players][round_index])

  def _CreateGameSettingObject(self):
    self._game_setting_obj = game_setting.GameSetting(self._number_of_players)

  def testEndOfRoundOnePlayer(self):
    self._number_of_players = 1
    self._TestEndOfRound()

  def testEndOfRoundTwoPlayer(self):
    self._number_of_players = 2
    self._TestEndOfRound()

  def testEndOfRoundThreePlayer(self):
    self._number_of_players = 3
    self._TestEndOfRound()

  def testEndOfRoundFourPlayer(self):
    self._number_of_players = 4
    self._TestEndOfRound()

  def testEndOfRoundFivePlayer(self):
    self._number_of_players = 5
    self._TestEndOfRound()

  def testNumberOfTurns(self):
    self._CreateGameSettingObject()
    self.assertEqual(
        self._game_setting_obj.GetNumberOfTurns(),
        config.NUMBER_OF_TURNS)


if __name__ == '__main__':
  unittest.main()
