"""This module provides simple command line UI for picking resource."""

class SimpleUI(object):
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
    print output
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

  def AskUserInput(self):
    return input('Input selected item in format like "franc: 1, fish: 1"')

  def TakeUserInput(self, user_input):
    # Example user_input = "franc: 1, fish: 1, smoked_fish: 1"
    parsed_inputs = user_input.split(',')
    picked_dict = dict()
    for item_input in parsed_inputs:
      item_input = item_input.strip()
      element_argument, number = item_input.split(':')
      element_argument = element_argument.strip()
      number = int(number.strip())
      picked_dict[element_argument] = number
    self._picker.Pick(**picked_dict)
