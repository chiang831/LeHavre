"""Unittest for enter_building_handler."""
import unittest

from game import enter_building_handler
from game import entry_fee
from game import player
from game import resource
from game import resource_picker
from game.buildings import building

class TestEnterBuildingHandler(unittest.TestCase):
  def setUp(self):
    self._building = None
    self._player = None
    self._picker = None
    self._fee = None
    self._handler = None

  def _CreateBuilding(self):
    self._building = building.CreateBuilding(
        'building1', resource.Resource(wood=1, clay=1),
        10, self._fee)

  def _CreatePlayer(self):
    self._player = player.Player('Player1')
    self._player.AddResource(resource.Resource(fish=2))

  def _CreatePicker(self):
    self._picker = resource_picker.CreateResourcePickerForEntryFee(
        self._player.GetResource(), self._fee)

  def _CreateHandler(self):
    self._handler = enter_building_handler.EnterBuildingHandler(
        building_obj=self._building,
        player_obj=self._player,
        picker_obj=self._picker,
        )

  def testEnterBuilding(self):
    self._fee = entry_fee.EntryFee(franc=0, food=1)
    self._CreateBuilding()
    self._CreatePlayer()
    self._CreatePicker()
    self._CreateHandler()
    self._picker.Pick(fish=1)
    self._handler.EnterBuilding()
    self.assertEqual(self._player.GetWorkerPlace(), self._building.GetName())
    self.assertTrue(self._player.GetResource().Equal(resource.Resource(fish=1)))
    self.assertTrue(self._building.IsOccupied())
    self.assertEqual(self._building.GetCurrentWorker(), self._player.GetName())

  def testCanNotEnter(self):
    self._fee = entry_fee.EntryFee(franc=0, food=3)
    self._CreateBuilding()
    self._CreatePlayer()
    self._CreatePicker()
    with self.assertRaises(enter_building_handler.NotEnoughEntryFeeError):
      self._CreateHandler()

  def testNotPickedEnough(self):
    self._fee = entry_fee.EntryFee(franc=0, food=2)
    self._CreateBuilding()
    self._CreatePlayer()
    self._CreatePicker()
    self._CreateHandler()
    self._picker.Pick(fish=1)
    with self.assertRaises(enter_building_handler.NotPickedEnoughEntryFeeError):
      self._handler.EnterBuilding()

if __name__ == '__main__':
  unittest.main()
