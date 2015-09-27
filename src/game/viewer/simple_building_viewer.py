"""This module provides simple viewer for building."""

from game.viewer import simple_resource_viewer as resource_viewer

class SimpleBuildingViewer(object):
  def __init__(self, building):
    self._building = building 

  def Show(self):
    output = ''
    output += 'Building: %s\n' % self._building.GetName()
    output += 'Cost: %s\n' % resource_viewer.ShowResource(
        self._building.GetCost())
    output += 'Value: %s\n' % self._building.GetValue()
    fee = self._building.GetFee()
    output += 'Fee: food=%s, franc=%s\n' % (fee.food, fee.franc)
    output += 'Instruction: %s\n' % self._building.GetInstruction()

    return output

def ShowPlayer(player_obj):
  viewer = SimplePlayerViewer(player_obj)
  return viewer.Show()
