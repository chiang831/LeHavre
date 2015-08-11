"""This module handles checking if resource meets food requirement."""

import resource

class FoodCheckerError(Exception):
  pass

class FoodTooMuchError(FoodCheckerError):
  pass

class NotFoodError(FoodCheckerError):
  pass


# pylint: disable=R0903
class FoodChecker(object):
  def __init__(self, target):
    self._target = target
    self._res = None
    self._check_result = None

  def Check(self, res):
    self._res = res
    self._CheckNonFood()
    return self._CheckFoodNumber()

  def _CheckNonFood(self):
    resource_element_dict = self._res.GetNonZeroResourceElementDict()
    for element in resource_element_dict.values():
      if not element.GetUnitFoodValue():
        raise NotFoodError('Not a food: %s' % element.name)

  def _CheckFoodNumber(self):
    food = self._res.GetFoodValue()

    if food < self._target:
      return False

    elif food == self._target:
      return True

    # Resource contains too much food.
    # Check if we can put back some resource element.
    else:
      resource_number_dict = self._res.GetNonZeroResourceNumberDict()
      for key, value in resource_number_dict.iteritems():
        test_dict = dict(resource_number_dict)
        test_dict[key] = value - 1
        test_res = resource.CreateResourceFromDict(test_dict)
        if test_res.GetFoodValue() >= self._target:
          raise FoodTooMuchError('Too much resource')
      return True
