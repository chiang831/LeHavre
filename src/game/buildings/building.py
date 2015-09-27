"""This module provide the building base class."""

class Building(object):
  def __init__(self, name, cost, value, fee, instruction=None):
    self._name = name
    self._cost = cost
    self._value = value
    self._fee = fee
    self._instruction = instruction
    self._worker_name = None

  def GetName(self):
    return self._name

  def GetCost(self):
    return self._cost

  def GetValue(self):
    return self._value

  def GetFee(self):
    return self._fee

  def GetInstruction(self):
    return self._instruction

  def SetCurrentWorker(self, player_name):
    self._worker_name = player_name

  def IsOccupied(self):
    return self._worker_name is not None

  def GetCurrentWorker(self):
    return self._worker_name


def CreateBuilding(name, cost, value, fee):
  return Building(name, cost, value, fee)
