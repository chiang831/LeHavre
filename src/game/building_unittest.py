"""Unittest for building module."""

import unittest

import building
import resource

class TestBuilding(unittest.TestCase):
  def testCreateBuilding(self):
    res = resource.Resource(clay=1, wood=1)
    value = 10
    name = 'building1'
    fee = resource.Resource(franc=1)
    building_obj = building.CreateBuilding(
        name=name,
        cost=res,
        value=value,
        fee=fee)
    self.assertEqual(res, building_obj.GetCost())
    self.assertEqual(value, building_obj.GetValue())
    self.assertEqual(name, building_obj.GetName())
    self.assertEqual(fee, building_obj.GetFee())


if __name__ == '__main__':
  unittest.main()
