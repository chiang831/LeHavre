"""This module handles game setting for different number of players."""

from game import config

class GameSetting(object):
  """Provide game setting for different number of players."""
  def __init__(self, number_of_players):
    self._number_of_players = number_of_players

  @classmethod
  def GetStartResourcesPilesDict(cls):
    """This start resources setting is the same for all number of players."""
    return config.START_RESOURCES_PILES

  @classmethod
  def GetLongGameStartingOffer(cls):
    return config.LONG_GAME_STARTING_OFFER

  def GetEndOfRound(self, round_index):
    return config.END_OF_ROUND_DICT[self._number_of_players][round_index]
  @classmethod
  def GetNumberOfTurns(cls):
    return config.NUMBER_OF_TURNS

  def GetStartingBuildings(self):
    return config.STARTING_BUILDINGS

