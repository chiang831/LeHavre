"""This module provide the building base class."""

class Building(object):
  def __init__(self, name, cost, value):
    self._name = name
    self._cost = cost
    self._value = value

  def GetName(self):
    return self._name

  def GetCost(self):
    return self._cost

  def GetValue(self):
    return self._value

def CreateBuilding(name, cost, value):
  return Building(name, cost, value)
