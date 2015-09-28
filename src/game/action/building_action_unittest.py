"""Unittest for building_action module."""

import unittest

from game import player
from game.action import building_action

class TestBuildingAction(unittest.TestCase):
  def setUp(self):
    self._player = player.Player('Player1')
    self._need_selection = False
    self._two_transactions = False
    self._action = None

  def _CreateAction(self):
    self._action = building_action.BuildingAction(
        player_obj=self._player,
        need_selection=self._need_selection,
        two_transactions=self._two_transactions)

  def testStartAction(self):
    self._CreateAction()
    self.assertFalse(self._action.IsDone())
    self._action.StartAction()
    self.assertTrue(self._action.IsDone())

  def testStartActionTransaction(self):
    self._need_selection = True
    self._CreateAction()
    self.assertFalse(self._action.IsDone())
    self._action.StartAction()
    self._action.Transaction()
    self.assertTrue(self._action.IsDone())

  def testStartActionTransactionEnd(self):
    self._need_selection = True
    self._two_transactions = True
    self._CreateAction()
    self.assertFalse(self._action.IsDone())
    self._action.StartAction()
    self._action.Transaction()
    self.assertFalse(self._action.IsDone())
    self._action.EndAction()
    self.assertTrue(self._action.IsDone())

  def testStartActionTransactionTransaction(self):
    self._need_selection = True
    self._two_transactions = True
    self._CreateAction()
    self.assertFalse(self._action.IsDone())
    self._action.StartAction()
    self._action.Transaction()
    self.assertFalse(self._action.IsDone())
    self._action.Transaction()
    self.assertTrue(self._action.IsDone())

  def testInvalidTransactionBeforeStart(self):
    self._need_selection = True
    self._two_transactions = True
    self._CreateAction()
    with self.assertRaises(building_action.BuildingActionError):
      self._action.Transaction()

  def testInvalidEndBeforeTransaction(self):
    self._need_selection = True
    self._two_transactions = True
    self._CreateAction()
    self._action.StartAction()
    with self.assertRaises(building_action.BuildingActionError):
      self._action.EndAction()

  def testInvalidEndBeforeTransaction(self):
    self._need_selection = True
    self._two_transactions = True
    self._CreateAction()
    self._action.StartAction()
    with self.assertRaises(building_action.BuildingActionError):
      self._action.EndAction()

  def testInvalidTranactionTwice(self):
    self._need_selection = True
    self._two_transactions = False
    self._CreateAction()
    self._action.StartAction()
    self._action.Transaction()
    with self.assertRaises(building_action.BuildingActionError):
      self._action.Transaction()

  def testInvalidEndAction(self):
    self._CreateAction()
    self._action.StartAction()
    with self.assertRaises(building_action.BuildingActionError):
      self._action.EndAction()

  def testInvalidEndActionAfterTransaction(self):
    self._need_selection = True
    self._CreateAction()
    self._action.StartAction()
    self._action.Transaction()
    with self.assertRaises(building_action.BuildingActionError):
      self._action.EndAction()

  def testInvalidActionAfterDone(self):
    self._need_selection = True
    self._two_transactions = True
    self._CreateAction()
    self._action.StartAction()
    self._action.Transaction()
    self._action.Transaction()
    with self.assertRaises(building_action.BuildingActionError):
      self._action.StartAction()
    with self.assertRaises(building_action.BuildingActionError):
      self._action.Transaction()
    with self.assertRaises(building_action.BuildingActionError):
      self._action.EndAction()

  def testInvalidStartActionTwice(self):
    self._need_selection = True
    self._CreateAction()
    self._action.StartAction()
    with self.assertRaises(building_action.BuildingActionError):
      self._action.StartAction()

if __name__ == '__main__':
  unittest.main()
