"""Unittest for simple_resource_picker_viewer module."""

import unittest

from game import resource
from game import resource_picker

from game import simple_resource_picker_viewer

class TestSimpleViewernittest(unittest.TestCase):
  def setUp(self):
    self._resource_picker = resource_picker.ResourcePicker()
    self._viewer = simple_resource_picker_viewer.SimpleResourcePickerViewer(
        self._resource_picker)
    self._res = None

  def _SetAvailableResource(self):
    self._resource_picker.SetAvailableResource(self._res)

  def testShowUI(self):
    self._res = resource.Resource(franc=1, fish=1)
    self._SetAvailableResource()
    output = self._viewer.ShowResources()
    expected_output = 'Select from available resource: Franc: 1, Fish: 1.'
    self.assertEqual(output, expected_output)

  def testShowUISmokedFish(self):
    self._res = resource.Resource(franc=1, fish=1, smoked_fish=1)
    self._SetAvailableResource()
    output = self._viewer.ShowResources()
    expected_output = ('Select from available resource: '
                       'Franc: 1, Fish: 1, Smoked Fish: 1.')
    self.assertEqual(output, expected_output)

  def testShowPicked(self):
    self._res = resource.Resource(franc=1, fish=1, smoked_fish=1)
    self._SetAvailableResource()
    self._resource_picker.Pick(franc=1, fish=1, smoked_fish=1)
    output = self._viewer.ShowPicked()
    expected_output = ('You already picked: '
                       'Franc: 1, Fish: 1, Smoked Fish: 1.')
    self.assertEqual(output, expected_output)

  def ShowPickedFoodValue(self):
    self._res = resource.Resource(franc=1, fish=1, smoked_fish=1)
    self._SetAvailableResource()
    self._resource_picker.Pick(franc=1, fish=1, smoked_fish=1)
    output = self._viewer.ShowPickedFoodValue()
    expected_output = ('Picked food value: 4')
    self.assertEqual(output, expected_output)

  def testShow(self):
    self._res = resource.Resource(franc=1, fish=1, smoked_fish=1)
    self._SetAvailableResource()
    self._resource_picker.Pick(franc=1, fish=1, smoked_fish=1)
    output = self._viewer.Show()
    expected_output = ('Select from available resource: '
                       'Franc: 1, Fish: 1, Smoked Fish: 1.\n')
    expected_output += ('You already picked: '
                        'Franc: 1, Fish: 1, Smoked Fish: 1.\n')
    expected_output += ('Picked food value: 4')
    self.assertEqual(output, expected_output)


if __name__ == '__main__':
  unittest.main()
