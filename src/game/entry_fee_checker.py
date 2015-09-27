"""Module for checking entry fee."""

from game import food_checker
from game import resource

class TooMuchError(Exception):
  pass

class FrancTooMuchError(TooMuchError):
  pass

class FoodTooMuchError(TooMuchError):
  pass

# pylint: disable=R0903
class EntryFeeChecker(object):
  def __init__(self, fee):
    self._fee = fee

  def Check(self, res):
    test_res = res.Copy()
    res_franc = test_res.GetResourceNumberByName('franc')
    if res_franc < self._fee.franc:
      return False
    elif res_franc > self._fee.franc:
      if not self._fee.food:
        raise FrancTooMuchError(
            '%d franc is greater than needed %d franc' %
            (res_franc, self._fee.franc))
    else:
      if not self._fee.food:
        return True

    test_res.Subtract(resource.Resource(franc=self._fee.franc))

    food_checker_obj = food_checker.FoodChecker(self._fee.food)
    result = None
    try:
      result = food_checker_obj.Check(test_res)
    except food_checker.FoodTooMuchError, message:
      raise FoodTooMuchError(message)
    return result
