"""This module provides simple viewer for picking resource."""

class SimpleResourcePickerViewer(object):
  def __init__(self, resource_picker):
    self._picker = resource_picker

  def _ShowElementsInResource(self, res_to_show):
    output = ''
    res_elements = res_to_show.GetNonZeroResourceElementDict().values()
    for idx, element in enumerate(res_elements):
      output += ' %s: %d' % (element.name, element.GetNumber())
      if idx == len(res_elements) - 1:
        output += '.'
      else:
        output += ','
    return output

  def Show(self):
    output = ''
    output += self.ShowResources() + '\n'
    output += self.ShowPicked() + '\n'
    output += self.ShowPickedFoodValue()
    return output

  def ShowResources(self):
    # Example output:
    # "Select from available resource: Franc: 1, Fish: 1."
    output = 'Select from available resource:'
    res_to_show = self._picker.GetAvailableResource()
    output += self._ShowElementsInResource(res_to_show)
    return output

  def ShowPicked(self):
    output = 'You already picked:'
    res_to_show = self._picker.GetPicked()
    output += self._ShowElementsInResource(res_to_show)
    return output

  def ShowPickedFoodValue(self):
    output = 'Picked food value: '
    picked_res= self._picker.GetPicked()
    food_value = picked_res.GetFoodValue()
    output += str(food_value)
    return output
