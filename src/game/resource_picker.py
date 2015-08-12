"""This module handles picking resource from available resource."""

import resource

class ResourcePickerError(Exception):
  pass

class ResourcePicker(object):
  def __init__(self):
    self._available = None
    self._picked_resource = resource.Resource()

  def SetAvailableResource(self, res):
    self._available = res

  def GetAvailableResource(self):
    return self._available

  def Pick(self, **kwargs):
    resource_to_pick = resource.Resource(**kwargs)
    if not self._CanPick(resource_to_pick):
      raise ResourcePickerError('Not enough resource: %r' % kwargs)
    self._picked_resource.Add(resource_to_pick)

  def _CanPick(self, resource_to_pick):
    total_picked = self._picked_resource.Copy()
    total_picked.Add(resource_to_pick)
    for key, elem in total_picked.GetNonZeroResourceElementDict().iteritems():
      available_value = self._available.GetResourceNumberByName(key)
      if elem.GetNumber() > available_value:
        return False
    return True

  def GetPicked(self):
    return self._picked_resource


class ResourcePickerForTest(ResourcePicker):
  def Pick(self, **kwargs):
    return

  def SetPickedResource(self, res):
    self._picked_resource = res
