"""This module provide the building base class."""

class Building(object):
  def __init__(self, name, cost, value, fee):
    self._name = name
    self._cost = cost
    self._value = value
    self._fee = fee

  def GetName(self):
    return self._name

  def GetCost(self):
    return self._cost

  def GetValue(self):
    return self._value

  def GetFee(self):
    return self._fee

def CreateBuilding(name, cost, value, fee):
  return Building(name, cost, value, fee)
