import game_setting
import resource

class GameFlow(object):
  def __init__(self, setting):
    self._resource_pile = resource.CreateResourceFromDict(
        setting.GetStartResourcesPilesDict())
    self._players = list()

  def GetResourcePile(self):
    return self._resource_pile

  def AddPlayer(self, new_player):
    self._players.append(new_player)

  def GetPlayer(self, name):
    for p in self._players:
      if p.GetName() == name:
        return p

def CreateGameFlow(setting):
  return GameFlow(setting)
