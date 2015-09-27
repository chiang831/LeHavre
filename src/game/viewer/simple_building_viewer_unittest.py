"""Unittest for simple_building_viewer."""

import unittest

from game import resource
from game import entry_fee

from game.buildings import building
from game.viewer import simple_building_viewer
from game.viewer import simple_resource_viewer

class TestBuildingViewer(unittest.TestCase):
  def setUp(self):
    self._name = 'TestBuilding'
    self._cost= resource.Resource(wood=1, clay=1)
    self._value = 10
    self._fee = entry_fee.EntryFee(food=1, franc=1)
    self._instruction = 'instruction'
    self._expected_output = None
    self._building = building.Building(
        self._name, self._cost, self._value, self._fee, self._instruction)

  def _SetExpectedOutput(self):
    self._expected_output = 'Building: %s\n' % self._name
    res_viewer = simple_resource_viewer.SimpleResourceViewer()
    res_viewer.SetResource(self._cost)
    self._expected_output += 'Cost: %s\n' % res_viewer.Show()
    self._expected_output += 'Value: %s\n' % self._value
    self._expected_output += 'Fee: food=%s, franc=%s\n' % (
        self._fee.food, self._fee.franc)
    self._expected_output += 'Instruction: %s\n' % self._instruction

  def testBuildingViewer(self):
    self._SetExpectedOutput()
    building_viewer = simple_building_viewer.SimpleBuildingViewer(
        self._building)
    self.assertEqual(self._expected_output, building_viewer.Show())


if __name__ == '__main__':
  unittest.main()
