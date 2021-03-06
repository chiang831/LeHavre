"""Unittest for resource_picker module."""

import unittest

from game import entry_fee
from game import resource
from game import resource_picker

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

  def testPickOneFrancThenOneFishThenOneFranc(self):
    self._picker.SetAvailableResource(resource.Resource(franc=2, fish=1))
    self._picker.Pick(franc=1)
    self._picker.Pick(fish=1)
    self._picker.Pick(franc=1)
    expected_res = resource.Resource(franc=2, fish=1)
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

  def testUnpick(self):
    self._picker.SetAvailableResource(resource.Resource(franc=2, fish=1))
    self._picker.Pick(franc=2)
    self._picker.Pick(fish=1)
    self._picker.Unpick(franc=1)
    self.assertTrue(
        self._picker.GetPicked().Equal(resource.Resource(franc=1, fish=1)))

  def testInvalidUnpick(self):
    self._picker.SetAvailableResource(resource.Resource(franc=2, fish=1))
    with self.assertRaises(resource_picker.ResourcePickerError):
      self._picker.Unpick(franc=1)

    self._picker.Pick(franc=1)
    with self.assertRaises(resource_picker.ResourcePickerError):
      self._picker.Unpick(franc=2)


class TestCreateResourcePicker(unittest.TestCase):
  def testCreateResourcePickerForFood(self):
    res = resource.Resource(franc=1, fish=1, clay=1)
    picker_obj = resource_picker.CreateResourcePickerForFood(res)
    self.assertTrue(
        picker_obj.GetAvailableResource().Equal(
            resource.Resource(franc=1, fish=1)))

  def testCreateResourcePickerForEntryFeeOnlyFranc(self):
    res = resource.Resource(franc=1, fish=1, clay=1)
    fee = entry_fee.EntryFee(franc=1, food=0)
    picker_obj = resource_picker.CreateResourcePickerForEntryFee(res, fee)
    self.assertTrue(
        picker_obj.GetAvailableResource().Equal(
            resource.Resource(franc=1)))

  def testCreateResourcePickerForEntryFee(self):
    res = resource.Resource(franc=1, fish=1, clay=1)
    fee = entry_fee.EntryFee(franc=1, food=1)
    picker_obj = resource_picker.CreateResourcePickerForEntryFee(res, fee)
    self.assertTrue(
        picker_obj.GetAvailableResource().Equal(
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
