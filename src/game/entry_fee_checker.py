"""Module for checking entry fee."""

import food_checker
import resource

# pylint: disable=R0903
class EntryFeeChecker(object):
  def __init__(self, fee):
    self._fee = fee

  def Check(self, res):
    test_res = res.Copy()
    res_franc = test_res.GetResourceNumberByName('franc')
    if res_franc < self._fee.franc:
      return False

    test_res.Subtract(resource.Resource(franc=self._fee.franc))

    food_checker_obj = food_checker.FoodChecker(self._fee.food)
    return food_checker_obj.Check(test_res)
