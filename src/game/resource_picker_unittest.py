"""Unittest for resource_picker module."""

import unittest

import resource
import resource_picker

class TestResourcePicker(unittest.TestCase):
  def setUp(self):
    self._picker = resource_picker.ResourcePicker()

  def testPickOneFranc(self):
    self._picker.SetAvailableResource(resource.Resource(franc=1))
    self._picker.Pick(franc=1)
    expected_res = resource.Resource(franc=1)
    self.assertTrue(self._picker.GetPicked().Equal(expected_res))

  def testPickOneFrancOneFish(self):
    self._picker.SetAvailableResource(resource.Resource(franc=1, fish=1))
    self._picker.Pick(franc=1, fish=1)
    expected_res = resource.Resource(franc=1, fish=1)
    self.assertTrue(self._picker.GetPicked().Equal(expected_res))

  def testPickInvalid(self):
    self._picker.SetAvailableResource(resource.Resource(franc=1, fish=1))
    with self.assertRaises(resource_picker.ResourcePickerError):
      self._picker.Pick(clay=1)

  def testGetAvailable(self):
    self._picker.SetAvailableResource(resource.Resource(franc=1, fish=1))
    self.assertTrue(
        self._picker.GetAvailableResource().Equal(
            resource.Resource(franc=1, fish=1)))


class TestResourcePickerForTest(unittest.TestCase):
  def setUp(self):
    self._picker = resource_picker.ResourcePickerForTest()

  def testSetPickedResource(self):
    expected_res = resource.Resource(franc=1)
    self._picker.SetPickedResource(expected_res)

    # These calls will NOT change GetPicked result because a
    # ResourcePickerForTest method always returns set in
    # SetPickedResource(expected_res)
    self._picker.Pick(franc=2)
    self._picker.Pick(fish=3)

    self.assertTrue(self._picker.GetPicked().Equal(expected_res))


if __name__ == '__main__':
  unittest.main()
