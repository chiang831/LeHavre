import game_setting
import resource

class GameFlow(object):
  def __init__(self, setting):
    self._setting = setting
    self._resource_pile = resource.CreateResourceFromDict(
        setting.GetStartResourcesPilesDict())
    self._players = list()
    self._resource_generators = list()
    self._turn_index = 0

  def GetResourcePile(self):
    return self._resource_pile

  def AddPlayer(self, new_player):
    self._players.append(new_player)

  def GetPlayer(self, name):
    for p in self._players:
      if p.GetName() == name:
        return p

  def StartingOffer(self):
    starting_offer_dict = self._setting.GetLongGameStartingOffer()
    starting_offer = resource.CreateResourceFromDict(starting_offer_dict)
    for p in self._players:
      p.AddResource(starting_offer)

  def SetResourceGenerators(self, res_gen_list):
    self._resource_generators = res_gen_list

  def GenerateResource(self):
    self._resource_pile.Add(
        self._resource_generators[self._turn_index].GetResource())

  def NextTurn(self):
    self._turn_index = self._turn_index + 1


def CreateGameFlow(setting):
  return GameFlow(setting)
