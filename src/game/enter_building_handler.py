"""Module to handle entering building"""

from game import entry_fee_checker

class AlreadyOccupiedError(Exception):
  pass

class NotEnoughEntryFeeError(Exception):
  pass

class NotPickedEnoughEntryFeeError(Exception):
  pass

class EnterBuildingHandler(object):
  def __init__(self, building_obj, player_obj, picker_obj):
    self._building = building_obj
    self._player = player_obj
    self._picker = picker_obj
    self._checker = None
    self._picked_res = None
    self._CreateChecker()
    self._CheckCanEnter()
    if building_obj.IsOccupied():
      raise AlreadyOccupiedError(
          'Building %s is occupied' % self._building.GetName())

  def _CreateChecker(self):
    self._checker = entry_fee_checker.EntryFeeChecker(self._building.GetFee())

  def _CheckCanEnter(self):
    all_picked_res = self._player.GetResource().Copy()
    can_enter = False
    try:
      can_enter = self._checker.Check(all_picked_res)
    # Too much is ok since we just check that player has enough resource to
    # pay entry fee.
    except entry_fee_checker.TooMuchError:
      can_enter = True
    if not can_enter:
      raise NotEnoughEntryFeeError('Not enough resource for entry fee.')

  def EnterBuilding(self):
    self._picked_res = self._picker.GetPicked()
    self._CheckPickedEnough()
    self._PayEntryFee()
    self._OccupyBuilding()

  def _CheckPickedEnough(self):
    can_enter = self._checker.Check(self._picked_res)
    if not can_enter:
      raise NotPickedEnoughEntryFeeError(
          'Not picked enough resource for entry fee')

  def _PayEntryFee(self):
    self._player.SubtractResource(self._picked_res)

  def _OccupyBuilding(self):
    self._player.SetWorkerPlace(self._building.GetName())
    self._building.SetCurrentWorker(self._player.GetName())
