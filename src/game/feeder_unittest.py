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

  def _SetFoodAndPlayer(self):
    self._feeder.SetFoodRequirement(self._food_req)
    self._feeder.SetPlayer(self._player)

  def _SetPickedResource(self):
    self._resource_picker_for_test.SetPickedResource(self._picked_res)

  def testGetResourcePicker(self):
    self.assertEqual(
        self._feeder.GetResourcePicker(), self._resource_picker_for_test)

  def testFeedByFish(self):
    self._food_req = 2
    self._available_res = resource.Resource(fish=2)
    self._SetAvailableResource()
    self._SetFoodAndPlayer()
    self._picked_res = resource.Resource(fish=2)
    self._SetPickedResource()

    self._feeder.FeedWithPickedResource()
    self.assertTrue(
        self._player.GetResource().Equal(
            resource.Resource()))

  def testCanGiveMoreFoodError(self):
    self._food_req = 2
    self._available_res = resource.Resource(fish=2)
    self._SetAvailableResource()
    self._SetFoodAndPlayer()
    self._picked_res = resource.Resource(fish=1)
    self._SetPickedResource()

    with self.assertRaises(feeder.FeederError):
      self._feeder.FeedWithPickedResource()

  def testNotEnoughFoodGetLoan(self):
    self._food_req = 4
    self._available_res = resource.Resource(fish=1, franc=1)
    self._SetAvailableResource()
    self._SetFoodAndPlayer()
    self._picked_res = resource.Resource(fish=1, franc=1)
    self._SetPickedResource()
    self._feeder.FeedWithPickedResource()

    self.assertTrue(
        self._player.GetResource().Equal(
            resource.Resource(loan=1, franc=2)))

  def TestGetFoodRequirement(self):
    self._food_req = 2
    self._SetFoodAndPlayer()
    self.assertEqual(self._food_req, self._feeder.GetFoodRequirement())


class TestCreateFeeder(unittest.TestCase):
  # pylint: disable=W0212
  def testCreateFeeder(self):
    player_obj = player.Player('Player1')
    picker_obj = resource_picker.ResourcePicker()
    food_req = 1
    feeder_obj = feeder.CreateFeeder(player_obj, food_req, picker_obj)
    self.assertEqual(feeder_obj._player, player_obj)
    self.assertEqual(feeder_obj._resource_picker, picker_obj)
    self.assertEqual(feeder_obj._food_req, food_req)


if __name__ == '__main__':
  unittest.main()
