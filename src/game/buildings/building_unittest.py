"""Unittest for building module."""

import unittest

from game import resource
from game import entry_fee
from game.buildings import building

class TestBuilding(unittest.TestCase):
  def setUp(self):
    self._res = None
    self._value = None
    self._name = None
    self._fee = None
    self._building_obj = None

  def _CreateBuilding(self):
    self._res = resource.Resource(clay=1, wood=1)
    self._value = 10
    self._name = 'building1'
    self._fee = entry_fee.EntryFee(franc=1, food=1)
    self._building_obj = building.CreateBuilding(
        name=self._name,
        cost=self._res,
        value=self._value,
        fee=self._fee)

  def testCreateBuilding(self):
    self._CreateBuilding()
    self.assertEqual(self._res, self._building_obj.GetCost())
    self.assertEqual(self._value, self._building_obj.GetValue())
    self.assertEqual(self._name, self._building_obj.GetName())
    self.assertEqual(self._fee, self._building_obj.GetFee())

  def testIsOccupied(self):
    self._CreateBuilding()
    self._building_obj.SetCurrentWorker('player1')
    self.assertTrue(self._building_obj.IsOccupied())
    self.assertEqual(self._building_obj.GetCurrentWorker(), 'player1')

if __name__ == '__main__':
  unittest.main()
