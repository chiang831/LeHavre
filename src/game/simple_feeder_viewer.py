"""This module provides simple viewer for feeder."""

import simple_resource_picker_viewer as picker_viewer

class SimpleFeederViewer(object):
  def __init__(self, feeder):
    self._feeder = feeder
    self._picker_viewer = picker_viewer.SimpleResourcePickerViewer(
        self._feeder.GetResourcePicker())

  def Show(self):
    output = ''
    output += 'Need to feed: %d food\n' % self._feeder.GetFoodRequirement()
    output += self._picker_viewer.Show()
    return output

def ShowFeeder(feeder_obj):
  viewer = SimpleFeederViewer(feeder_obj)
  return viewer.Show()
