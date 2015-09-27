"""Module for building firm 1."""

from game import entry_fee
from game import resource
from game.buildings import building

class BuildingFirm1(building.Building):
  _NAME = 'BuildingFirm1'
  _COST = None
  _VALUE = 4
  _FEE = entry_fee.EntryFee(franc=0, food=0)

  def __init__():
    super(BuildingFirm1, self).__init__(
        name=_NAME,
        cost=_COST,
        value=_VALUE,
        fee=_FEE)
