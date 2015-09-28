"""This module provides simple viewer for building."""

from game.viewer import simple_resource_viewer as resource_viewer

class SimpleBuildingViewer(object):
  def __init__(self, building):
    self._building = building 

  def Show(self):
    output = ''
    output += 'Name: %s\n' % self._building.GetName()
    output += 'Cost: %s\n' % resource_viewer.ShowResource(
        self._building.GetCost())
    output += 'Value: %s\n' % self._building.GetValue()
    output += _ShowEntryFee(self._building.GetFee())
    output += 'Instruction: %s\n' % self._building.GetInstruction()
    if self._building.IsOccupied():
      output += 'Occupied by: %s\n' % self._building.GetCurrentWorker()

    return output

def _ShowEntryFee(fee):
  output = 'Fee: '
  if fee.food and fee.franc:
    output += '%d food, %d franc' % (fee.food, fee.franc)
  elif fee.food:
    output += '%d food' % fee.food
  elif fee.franc:
    output += '%d franc' % fee.franc
  output += '\n'
  return output
