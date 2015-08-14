"""This module handles feeding food to worker in the end of a round."""

import food_checker
import resource


class FeederError(Exception):
  pass

class Feeder(object):
  def __init__(self):
    self._resource_picker = None
    self._player = None
    self._food_req = None
    self._food_checker = None
    self._picked_res = None

  def SetResourcePicker(self, picker):
    self._resource_picker = picker

  def SetPlayer(self, player):
    self._player = player

  def SetFoodRequirement(self, food_requirement):
    self._food_req = food_requirement
    self._food_checker = food_checker.FoodChecker(self._food_req)

  def FeedWithPickedResource(self):
    self._picked_res = self._resource_picker.GetPicked()
    try:
      enough = self._food_checker.Check(self._picked_res)
    except food_checker.FoodTooMuchError:
      raise FeederError('Pick too much')
    except food_checker.NotFoodError:
      raise FeederError('Pick non food')
    if enough:
      self._ApplyTransaction()
    else:
      self._CheckReallyCanNotPayMore()
      self._ApplyTransaction()
      self._ApplyLoan()

  def _ApplyTransaction(self):
    self._player.SubtractResource(self._picked_res)

  def _CheckReallyCanNotPayMore(self):
    test_res = self._player.GetResource().Copy()
    test_res.Subtract(self._picked_res)
    if test_res.GetFoodValue():
      raise FeederError('Can pay more')

  @classmethod
  def _GetNeededLoanNumber(cls, needed_loan_value):
    loan_unit_value = resource.Loan.GetFrancValueWhenGetLoan()
    needed_loan_number = (
        needed_loan_value / loan_unit_value)
    if needed_loan_value % loan_unit_value:
      needed_loan_number = needed_loan_number + 1

    return needed_loan_number

  def _ApplyLoan(self):
    picked_food_value = self._picked_res.GetFoodValue()
    needed_loan_value = self._food_req - picked_food_value
    needed_loan_number = self._GetNeededLoanNumber(needed_loan_value)

    self._player.GetLoan(needed_loan_number)
    self._player.SubtractResource(
        resource.Resource(franc=needed_loan_value))
