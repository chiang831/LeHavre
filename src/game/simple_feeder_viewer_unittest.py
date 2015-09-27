"""Unittest for simple_feeder_viewer."""

import unittest

from game import feeder
from game import player
from game import resource
from game import resource_picker

from game import simple_feeder_viewer
from game import simple_resource_picker_viewer

class TestFeederViewer(unittest.TestCase):
  def setUp(self):
    self._food_requirement = None
    self._picker_obj = None
    self._feeder_obj = None
    self._expected_output = None

  def _CreateTestFeeder(self):
    res = resource.Resource(franc=1, fish=2, clay=1)
    player_obj = player.Player('Player1')
    player_obj.AddResource(res)
    self._food_requirement = 2
    self._picker_obj = resource_picker.CreateResourcePickerForFood(res)
    self._feeder_obj = feeder.CreateFeeder(
        player_obj, self._food_requirement, self._picker_obj)

  def _SetExpectedOutput(self):
    self._expected_output = 'Need to feed: %d food\n' % self._food_requirement
    picker_viewer = simple_resource_picker_viewer.SimpleResourcePickerViewer(
        self._picker_obj)
    self._expected_output += picker_viewer.Show()

  def testFeederViewer(self):
    self._CreateTestFeeder()
    self._SetExpectedOutput()
    feeder_viewer = simple_feeder_viewer.SimpleFeederViewer(self._feeder_obj)
    self.assertEqual(self._expected_output, feeder_viewer.Show())

  def testShowFeeder(self):
    self._CreateTestFeeder()
    self._SetExpectedOutput()
    self.assertEqual(
        self._expected_output,
        simple_feeder_viewer.ShowFeeder(self._feeder_obj))


if __name__ == '__main__':
  unittest.main()
