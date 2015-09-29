"""Unittest for building plan."""

import unittest

from game import entry_fee 
from game import resource 
from game.buildings import building
from game.buildings import building_plan


class TestBuildingPlan(unittest.TestCase):
  def setUp(self):
    self._building_queues = None
    self._plan = None

  def _CreateTestBuilding(self, name):
    return building.Building(
        name=name, cost=resource.Resource(), value=0,
        fee=entry_fee.EntryFee(franc=0, food=0))

  def _CreateTestBuildingQueues(self):
    self._building_queues = [
        [self._CreateTestBuilding('Building 1'),
         self._CreateTestBuilding('Building 4'),
        ],
        [self._CreateTestBuilding('Building 2'),
         self._CreateTestBuilding('Building 5'),
        ],
        [self._CreateTestBuilding('Building 3'),
         self._CreateTestBuilding('Building 6'),
        ]
    ]

  def _CreatePlan(self):
    self._CreateTestBuildingQueues()
    self._plan = building_plan.BuildingPlan(
        self._building_queues)

  def testGetPlans(self):
    self._CreatePlan()
    plans = self._plan.GetPlans()
    self.assertEqual(plans[0].GetName(), 'Building 1')
    self.assertEqual(plans[1].GetName(), 'Building 2')
    self.assertEqual(plans[2].GetName(), 'Building 3')

  def testRemove(self):
    self._CreatePlan()
    self._plan.Remove('Building 1')
    plans = self._plan.GetPlans()
    self.assertEqual(plans[0].GetName(), 'Building 4')
    self.assertEqual(plans[1].GetName(), 'Building 2')
    self.assertEqual(plans[2].GetName(), 'Building 3')

  def testGetFromQueueNothing(self):
    self._CreatePlan()
    self._plan.Remove('Building 1')
    self._plan.Remove('Building 4')
    plans = self._plan.GetPlans()
    self.assertEqual(plans[0].GetName(), 'Building 2')
    self.assertEqual(plans[1].GetName(), 'Building 3')

  def testInvalidRemove(self):
    self._CreatePlan()
    with self.assertRaises(building_plan.BuildingPlanError):
      self._plan.Remove('Building 4')

  def testGetAllPlans(self):
    self._CreatePlan()
    all_plans = self._plan.GetAllPlans()
    self.assertEqual(all_plans, self._building_queues)


if __name__ == '__main__':
  unittest.main()
