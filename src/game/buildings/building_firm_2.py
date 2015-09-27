"""Module for building firm 2."""

from game import entry_fee
from game import resource
from game.buildings import building

class BuildingFirm2(building.Building):
  _NAME = 'BuildingFirm2'
  _COST = None
  _VALUE = 6
  _FEE = entry_fee.EntryFee(franc=0, food=1)

  def __init__(self):
    super(BuildingFirm2, self).__init__(
        name=self._NAME,
        cost=self._COST,
        value=self._VALUE,
        fee=self._FEE)
