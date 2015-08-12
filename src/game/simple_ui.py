"""This module provides simple command line UI for picking resource."""

class SimpleUI(object):
  def __init__(self, resource_picker):
    self._picker = resource_picker

  def ShowResources(self):
    # Example output:
    # "Select from available resource: Franc: 1, Fish: 1."
    output = 'Select from available resource:'
    res_to_show = self._picker.GetAvailableResource()
    res_elements = res_to_show.GetNonZeroResourceElementDict().values()
    for idx, element in enumerate(res_elements):
      output += ' %s: %d' % (element.name, element.GetNumber())
      if idx == len(res_elements) - 1:
        output += '.'
      else:
        output += ','
    print output
    return output

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
