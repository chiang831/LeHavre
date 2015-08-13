"""Unittest for simple_ui module."""

import unittest

import resource
import simple_ui
import resource_picker

class SimpleUIUnittest(unittest.TestCase):
  def setUp(self):
    self._resource_picker = resource_picker.ResourcePicker()
    self._ui = simple_ui.SimpleUI(self._resource_picker)
    self._res = None

  def _SetAvailableResource(self):
    self._resource_picker.SetAvailableResource(self._res)

  def testShowUI(self):
    self._res = resource.Resource(franc=1, fish=1)
    self._SetAvailableResource()
    output = self._ui.ShowResources()
    expected_output = 'Select from available resource: Franc: 1, Fish: 1.'
    self.assertEqual(output, expected_output)

  def testShowUISmokedFish(self):
    self._res = resource.Resource(franc=1, fish=1, smoked_fish=1)
    self._SetAvailableResource()
    output = self._ui.ShowResources()
    expected_output = ('Select from available resource: '
                       'Franc: 1, Fish: 1, Smoked Fish: 1.')
    self.assertEqual(output, expected_output)

  def testShowPicked(self):
    self._res = resource.Resource(franc=1, fish=1, smoked_fish=1)
    self._SetAvailableResource()
    self._resource_picker.Pick(franc=1, fish=1, smoked_fish=1)
    output = self._ui.ShowPicked()
    expected_output = ('You already picked: '
                       'Franc: 1, Fish: 1, Smoked Fish: 1.')
    self.assertEqual(output, expected_output)

  def testTakeUserInput(self):
    self._res = resource.Resource(franc=1, fish=1, clay=1)
    self._SetAvailableResource()
    # The name is the same as arguments in resource.Resource.
    user_input = 'franc: 1, fish: 1'
    self._ui.TakeUserInput(user_input)
    expected_picked_res = resource.Resource(franc=1, fish=1)
    self.assertTrue(
        self._resource_picker.GetPicked().Equal(expected_picked_res))

  def testTakeUserInputSmokedFish(self):
    self._res = resource.Resource(franc=1, fish=1, smoked_fish=1)
    self._SetAvailableResource()
    user_input = 'franc: 1, fish: 1, smoked_fish: 1'
    self._ui.TakeUserInput(user_input)
    expected_picked_res = resource.Resource(franc=1, fish=1, smoked_fish=1)
    self.assertTrue(
        self._resource_picker.GetPicked().Equal(expected_picked_res))

  def testTakeUserInputInvalid(self):
    self._res = resource.Resource(franc=1, fish=1, clay=1)
    self._SetAvailableResource()
    user_input = 'franc: 1, fish: 1, smoked_fish: 1'
    with self.assertRaises(resource_picker.ResourcePickerError):
      self._ui.TakeUserInput(user_input)

if __name__ == '__main__':
  unittest.main()
