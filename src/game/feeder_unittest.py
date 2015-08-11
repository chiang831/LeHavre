"""Unittest for feeder module."""

import unittest

import resource
import resource_picker
import feeder
import player


class TestFeeder(unittest.TestCase):
  def setUp(self):
    self._feeder = feeder.Feeder()
    self._player = player.Player('Player1')
    self._resource_picker_for_test = resource_picker.ResourcePickerForTest()
    self._feeder.SetResourcePicker(self._resource_picker_for_test)
    self._available_res = None
    self._picked_res = None
    self._food_req = None

  def _SetAvailableResource(self):
    self._player.AddResource(self._available_res)

  def _SetPickedResource(self):
    self._resource_picker_for_test.SetPickedResource(self._picked_res)

  def testFeedByFish(self):
    self._food_req = 2
    self._available_res = resource.Resource(fish=2)
    self._SetAvailableResource()
    self._picked_res = resource.Resource(fish=2)
    self._SetPickedResource()

    self._feeder.Feed(self._player, self._food_req, use_ui=False)
    self.assertTrue(
        self._player.GetResource().Equal(
            resource.Resource()))

  def testCanGiveMoreFoodError(self):
    self._food_req = 2
    self._available_res = resource.Resource(fish=2)
    self._SetAvailableResource()
    self._picked_res = resource.Resource(fish=1)
    self._SetPickedResource()

    with self.assertRaises(feeder.FeederError):
      self._feeder.Feed(self._player, self._food_req, use_ui=False)

  def testNotEnoughFoodGetLoan(self):
    self._food_req = 4
    self._available_res = resource.Resource(fish=1, franc=1)
    self._SetAvailableResource()
    self._picked_res = resource.Resource(fish=1, franc=1)
    self._SetPickedResource()
    self._feeder.Feed(self._player, self._food_req, use_ui=False)

    self.assertTrue(
        self._player.GetResource().Equal(
            resource.Resource(loan=1, franc=2)))

if __name__ == '__main__':
  unittest.main()
