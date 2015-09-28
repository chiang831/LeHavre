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
    self._instruction = 'instruction'
    self._expected_output = None
    self._current_worker = None

  def _CreateTestBuilding(self):
    self._building = building.Building(
        self._name, self._cost, self._value, self._fee, self._instruction)
    if self._current_worker:
      self._building.SetCurrentWorker(self._current_worker)

  def _SetExpectedOutput(self):
    self._expected_output = 'Name: %s\n' % self._name
    res_viewer = simple_resource_viewer.SimpleResourceViewer()
    res_viewer.SetResource(self._cost)
    self._expected_output += 'Cost: %s\n' % res_viewer.Show()
    self._expected_output += 'Value: %s\n' % self._value
    self._expected_output += self._ExpectedFeeOutput()
    self._expected_output += 'Instruction: %s\n' % self._instruction
    if self._current_worker:
      self._expected_output += 'Occupied by: %s\n' % self._current_worker

  def _ExpectedFeeOutput(self):
    output = 'Fee: '
    if self._fee.food and self._fee.franc:
      output += '%d food, %d franc' % (self._fee.food, self._fee.franc)
    elif self._fee.food:
      output += '%d food' % self._fee.food
    elif self._fee.franc:
      output += '%d franc' % self._fee.franc
    output += '\n'
    return output

  def testBuildingViewerEntryFeeContainsBoth(self):
    self._fee = entry_fee.EntryFee(food=1, franc=1)
    self._CreateTestBuilding()
    self._SetExpectedOutput()
    building_viewer = simple_building_viewer.SimpleBuildingViewer(
        self._building)
    self.assertEqual(self._expected_output, building_viewer.Show())

  def testBuildingViewerEntryFeeContainsFranc(self):
    self._fee = entry_fee.EntryFee(food=0, franc=1)
    self._CreateTestBuilding()
    self._SetExpectedOutput()
    building_viewer = simple_building_viewer.SimpleBuildingViewer(
        self._building)
    self.assertEqual(self._expected_output, building_viewer.Show())

  def testBuildingViewerEntryFeeContainsFood(self):
    self._fee = entry_fee.EntryFee(food=1, franc=0)
    self._CreateTestBuilding()
    self._SetExpectedOutput()
    building_viewer = simple_building_viewer.SimpleBuildingViewer(
        self._building)
    self.assertEqual(self._expected_output, building_viewer.Show())

  def testBuildingViewerOccupied(self):
    self._fee = entry_fee.EntryFee(food=1, franc=1)
    self._current_worker = 'player1'
    self._CreateTestBuilding()
    self._SetExpectedOutput()
    building_viewer = simple_building_viewer.SimpleBuildingViewer(
        self._building)
    self.assertEqual(self._expected_output, building_viewer.Show())


if __name__ == '__main__':
  unittest.main()
