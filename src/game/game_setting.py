import config

class GameSetting(object):
  """Provide game setting for different number of players."""
  def __init__(self, number_of_players):
    self._number_of_players = number_of_players

  def GetStartResourcesPilesDict(self):
    """This start resources setting is the same for all number of players."""
    return config.START_RESOURCES_PILES

  def GetLongGameStartingOffer(self):
    return config.LONG_GAME_STARTING_OFFER

  def GetEndOfRound(self, round_index):
    return config.END_OF_ROUND_DICT[self._number_of_players][round_index]
