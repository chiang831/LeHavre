"""Unittest for building_factory module"""

import unittest

from game.buildings import building_factory

class TestBuidlingFactory(unittest.TestCase):
  def testBuilding(self):
    name = 'BuildingFirm1'
    building_obj = building_factory.CreateBuildingByName(name)
    self.assertEqual(building_obj.GetName(), name)

  def testBuildingError(self):
    name = 'BuidlingFirm3'
    with self.assertRaises(building_factory.CreateBuildingError):
      building_obj = building_factory.CreateBuildingByName(name)


if __name__ == '__main__':
  unittest.main()
