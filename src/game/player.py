"""This module handles player in the game."""

import resource

class PlayerError(Exception):
  pass


class NotEnoughMoneyForLoanError(PlayerError):
  pass


class ReturnTooManyLoanError(PlayerError):
  pass


class Player(object):
  def __init__(self, name):
    self._name = name
    self._resource = resource.Resource()
    self._worker_place = None

  def GetName(self):
    return self._name

  def GetResource(self):
    return self._resource

  def AddResource(self, add_resource):
    self._resource.Add(add_resource)

  def SubtractResource(self, sub_resource):
    self._resource.Subtract(sub_resource)

  def GetLoan(self, number):
    add_franc = number * resource.Loan.GetFrancValueWhenGetLoan()
    add_res = resource.Resource(franc=add_franc, loan=number)
    self.AddResource(add_res)

  def ReturnLoan(self, loan_to_return):
    loan = self._resource.GetResourceNumberByName('loan')
    if loan < loan_to_return:
      raise ReturnTooManyLoanError()

    franc_to_return = (
        loan_to_return * resource.Loan.GetFrancValueWhenReturnLoan())
    franc = self._resource.GetResourceNumberByName('franc')
    if franc < franc_to_return:
      raise NotEnoughMoneyForLoanError()

    res_to_subtract = resource.Resource(
        franc=franc_to_return, loan=loan_to_return)
    self.SubtractResource(res_to_subtract)

  def SetWorkerPlace(self, building_name):
    self._worker_place = building_name

  def GetWorkerPlace(self):
    return self._worker_place
