"""Module for construction firm."""

from game import entry_fee
from game import resource
from game.buildings import building

class ConstructionFirm(building.Building):
  _NAME = 'Construction Firm'
  _COST = resource.Resource()
  _VALUE = 8
  _FEE = entry_fee.EntryFee(franc=0, food=2)
  _INSTRUCTION = 'Build 1 or 2 buildings.'

  def __init__(self):
    super(ConstructionFirm, self).__init__(
        name=self._NAME,
        cost=self._COST,
        value=self._VALUE,
        fee=self._FEE,
        instruction=self._INSTRUCTION,
        )
