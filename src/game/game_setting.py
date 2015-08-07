import config

class GameSetting(object):
  """Provide game setting for different number of players."""
  def __init__(self):
    pass

  def GetStartResourcesPilesDict(self):
    """This start resources setting is the same for all number of players."""
    return config.START_RESOURCES_PILES

  def GetLongGameStartingOffer(self):
    return config.LONG_GAME_STARTING_OFFER
