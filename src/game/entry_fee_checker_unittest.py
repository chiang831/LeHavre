"""Unittest for entry_fee_checker module."""

import unittest

import entry_fee
import entry_fee_checker
import food_checker
import resource

class TestEntryFeeChecker(unittest.TestCase):
  def setUp(self):
    self._fee = entry_fee.EntryFee(franc=2, food=2)
    self._checker = entry_fee_checker.EntryFeeChecker(self._fee)
    self._res = None

  def testMeet(self):
    self._res = resource.Resource(franc=2, fish=2)
    self.assertTrue(self._checker.Check(self._res))

  def testNotMeet(self):
    self._res = resource.Resource(franc=1, fish=2)
    self.assertFalse(self._checker.Check(self._res))

  def testTooMuchFood(self):
    self._res = resource.Resource(franc=2, fish=3)
    with self.assertRaises(entry_fee_checker.FoodTooMuchError):
      self._checker.Check(self._res)

  def testNotFood(self):
    self._res = resource.Resource(franc=2, fish=3, wood=1)
    with self.assertRaises(food_checker.NotFoodError):
      self._checker.Check(self._res)

  def testTooMuchButNeeded(self):
    self._res = resource.Resource(franc=2, meat=1)
    self.assertTrue(self._checker.Check(self._res))

  def testFrancForFood(self):
    self._res = resource.Resource(franc=4)
    self.assertTrue(self._checker.Check(self._res))

  def testTooMuchFranc(self):
    self._fee = entry_fee.EntryFee(franc=2, food=0)
    self._checker = entry_fee_checker.EntryFeeChecker(self._fee)
    self._res = resource.Resource(franc=3)
    with self.assertRaises(entry_fee_checker.FrancTooMuchError):
      self._checker.Check(self._res)

  def testOnlyFranc(self):
    self._fee = entry_fee.EntryFee(franc=2, food=0)
    self._checker = entry_fee_checker.EntryFeeChecker(self._fee)
    self._res = resource.Resource(franc=2)
    self.assertTrue(self._checker.Check(self._res))


if __name__ == '__main__':
  unittest.main()
