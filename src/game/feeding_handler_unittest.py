"""Unittest for feeding_handler."""

import unittest

from game import feeder
from game import feeding_handler
from game import player
from game import resource
from game import resource_picker

class TestFeedingHandler(unittest.TestCase):
  def setUp(self):
    self._feeding_handler = feeding_handler.FeedingHandler()
    self._food_requirement = 4
    self._players = list()

  def _CreateTestObjForPlayer(self, name, res):
    player_obj = player.Player(name)
    player_obj.AddResource(res)
    picker_obj = resource_picker.CreateResourcePickerForFood(res)
    feeder_obj = feeder.CreateFeeder(
        player_obj, self._food_requirement, picker_obj)
    self._feeding_handler.AddFeeder(name, feeder_obj)

  def testCheckFeedWithPicked(self):
    name = 'Player1'
    res = resource.Resource(franc=1, fish=4)
    self._CreateTestObjForPlayer(name, res)
    picker_obj = self._feeding_handler.GetFeeder(name).GetResourcePicker()
    picker_obj.Pick(franc=1)
    picker_obj.Pick(fish=3)
    self.assertFalse(self._feeding_handler.IsPlayerDone(name))
    self._feeding_handler.FeedWithPicked(name)
    self.assertTrue(self._feeding_handler.IsPlayerDone(name))

  def testCheckAllDone(self):
    name1 = 'Player1'
    res = resource.Resource(franc=1, fish=4)
    self._CreateTestObjForPlayer(name1, res)
    picker_obj_1 = self._feeding_handler.GetFeeder(name1).GetResourcePicker()
    picker_obj_1.Pick(franc=1)
    picker_obj_1.Pick(fish=3)
    self._feeding_handler.FeedWithPicked(name1)

    name2 = 'Player2'
    res = resource.Resource(franc=0, fish=3)
    self._CreateTestObjForPlayer(name2, res)

    self.assertFalse(self._feeding_handler.IsAllDone())

    picker_obj_2 = self._feeding_handler.GetFeeder(name2).GetResourcePicker()
    picker_obj_2.Pick(franc=0)
    picker_obj_2.Pick(fish=3)
    self._feeding_handler.FeedWithPicked(name2)

    self.assertTrue(self._feeding_handler.IsAllDone())


if __name__ == '__main__':
  unittest.main()
