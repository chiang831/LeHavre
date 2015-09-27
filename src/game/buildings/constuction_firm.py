"""Module for construction firm."""

from game import entry_fee
from game import resource
from game.buildings import building

class BuildingFirm1(building.Building):
  _NAME = 'ConstructionFirm'
  _COST = None
  _VALUE = 8
  _FEE = entry_fee.EntryFee(franc=0, food=2)

  def __init__(self):
    super(BuildingFirm1, self).__init__(
        name=self._NAME,
        cost=self._COST,
        value=self._VALUE,
        fee=self._FEE)
