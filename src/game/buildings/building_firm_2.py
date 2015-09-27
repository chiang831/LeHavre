"""Module for building firm 2."""

from game import entry_fee
from game import resource
from game.buildings import building

class BuildingFirm2(building.Building):
  _NAME = 'Building Firm 2'
  _COST = resource.Resource()
  _VALUE = 6
  _FEE = entry_fee.EntryFee(franc=0, food=1)
  _INSTRUCTION = 'Build 1 building.'

  def __init__(self):
    super(BuildingFirm2, self).__init__(
        name=self._NAME,
        cost=self._COST,
        value=self._VALUE,
        fee=self._FEE,
        instruction=self._INSTRUCTION,
        )
