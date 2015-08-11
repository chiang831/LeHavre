"""Unittest for food_checker module."""
import unittest

import food_checker
import resource

class TestFoodChecker(unittest.TestCase):
  def setUp(self):
    # Initialize the targeted food to 2.
    self._target_food = 2
    self._food_checker = food_checker.FoodChecker(
        self._target_food)

  def testCheckEnoughFish(self):
    picked_res = resource.Resource(fish=2)
    self.assertTrue(self._food_checker.Check(picked_res))

  def testCheckEnoughFrancFish(self):
    picked_res = resource.Resource(franc=1, fish=1)
    self.assertTrue(self._food_checker.Check(picked_res))

  def testCheckNotEnough(self):
    picked_res = resource.Resource(fish=1)
    self.assertFalse(self._food_checker.Check(picked_res))

  def testCheckTooMuch(self):
    picked_res = resource.Resource(franc=1, fish=2)
    with self.assertRaises(food_checker.FoodTooMuchError):
      self._food_checker.Check(picked_res)

  def testCheckTooMuchButNeededMeal(self):
    picked_res = resource.Resource(meal=1)
    self.assertTrue(self._food_checker.Check(picked_res))

  def testCheckTooMuchButNeededBread(self):
    picked_res = resource.Resource(bread=1)
    self._target_food = 1
    self._food_checker = food_checker.FoodChecker(
        self._target_food)
    self.assertTrue(self._food_checker.Check(picked_res))

  def testCheckNonValid(self):
    picked_res = resource.Resource(franc=1, fish=1, clay=1)
    with self.assertRaises(food_checker.NotFoodError):
      self._food_checker.Check(picked_res)


if __name__ == '__main__':
  unittest.main()
