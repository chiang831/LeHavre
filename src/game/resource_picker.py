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
    return self._available.GreaterThan(total_picked)

  def Unpick(self, **kwargs):
    resource_to_unpick = resource.Resource(**kwargs)
    if not self._CanUnpick(resource_to_unpick):
      raise ResourcePickerError('Can not unpick resource: %r' % kwargs)
    self._picked_resource.Subtract(resource_to_unpick)

  def _CanUnpick(self, resource_to_unpick):
    return self._picked_resource.GreaterThan(resource_to_unpick)

  def GetPicked(self):
    return self._picked_resource


class ResourcePickerForTest(ResourcePicker):
  def Pick(self, **kwargs):
    return

  def SetPickedResource(self, res):
    self._picked_resource = res


def CreateResourcePickerForFood(res):
  res_filtered = resource.FilterResourceFood(res)
  picker = ResourcePicker()
  picker.SetAvailableResource(res_filtered)
  return picker
