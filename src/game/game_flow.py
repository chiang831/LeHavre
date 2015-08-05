import game_setting
import resource

class GameFlow(object):
  def __init__(self, setting):
    self._resource_pile = resource.CreateResourceFromDict(
        setting.GetStartResourcesPilesDict())

  def GetResourcePile(self):
    return self._resource_pile

def CreateGameFlow(setting):
  return GameFlow(setting)
