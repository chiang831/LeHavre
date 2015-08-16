"""This module handles feeding of multiple players."""


class FeedingHandler(object):
  def __init__(self):
    self._name_feeder_dict = dict()
    self._name_success_dict = dict()

  def AddFeeder(self, player_name, feeder_obj):
    self._name_feeder_dict[player_name] = feeder_obj
    self._name_success_dict[player_name] = False

  def GetResourcePicker(self, name):
    return self._name_feeder_dict[name].GetResourcePicker()

  def FeedWithPicked(self, name):
    # A player should only feed once.
    if not self._name_success_dict[name]:
      self._name_feeder_dict[name].FeedWithPickedResource()
    self._name_success_dict[name] = True

  def IsPlayerDone(self, name):
    return self._name_success_dict[name]

  def IsAllDone(self):
    return all(self._name_success_dict.values())
