"""Unittest for player module."""

import unittest

from game import player
from game import resource

class TestPlayer(unittest.TestCase):
  def setUp(self):
    self._name = 'Player1'
    self._player = player.Player(self._name)

  def testInitPlayer(self):
    self.assertEqual(self._player.GetName(), self._name)

  def testAddAndGetResource(self):
    res_dict_1 = dict(franc=1, wood=2)
    resource_1 = resource.CreateResourceFromDict(res_dict_1)
    res_dict_2 = dict(franc=1, clay=3)
    resource_2 = resource.CreateResourceFromDict(res_dict_2)
    res_dict_sum = dict(franc=2, wood=2, clay=3)
    resource_sum = resource.CreateResourceFromDict(res_dict_sum)

    self._player.AddResource(resource_1)
    self._player.AddResource(resource_2)
    self.assertTrue(resource_sum.Equal(self._player.GetResource()))

  def testSubtract(self):
    res_dict_1 = dict(franc=2, fish=3)
    resource_1 = resource.CreateResourceFromDict(res_dict_1)
    res_dict_2 = dict(franc=1, fish=1)
    resource_2 = resource.CreateResourceFromDict(res_dict_2)
    res_dict_sub = dict(franc=1, fish=2)
    resource_sub = resource.CreateResourceFromDict(res_dict_sub)

    self._player.AddResource(resource_1)
    self._player.SubtractResource(resource_2)
    self.assertTrue(resource_sub.Equal(self._player.GetResource()))


class TestGetLoan(unittest.TestCase):
  def setUp(self):
    self._name = 'Player1'
    self._player = player.Player(self._name)

  def testGetLoan(self):
    res = resource.Resource(franc=0, fish=1)
    self._player.AddResource(res)
    self._player.GetLoan(1)
    self.assertTrue(
        self._player.GetResource().Equal(
            resource.Resource(franc=4, fish=1, loan=1)))

  def testReturnLoanNoLoan(self):
    res = resource.Resource(franc=0, fish=1)
    self._player.AddResource(res)
    with self.assertRaises(player.ReturnTooManyLoanError):
      self._player.ReturnLoan(1)

  def testReturnLoanNotEnoughMoney(self):
    res = resource.Resource(franc=0, fish=1)
    self._player.AddResource(res)
    self._player.GetLoan(2)
    self.assertTrue(
        self._player.GetResource().Equal(
            resource.Resource(franc=8, fish=1, loan=2)))
    with self.assertRaises(player.NotEnoughMoneyForLoanError):
      self._player.ReturnLoan(2)

  def testReturnLoanEnoughMoney(self):
    res = resource.Resource(franc=0, fish=1)
    self._player.AddResource(res)
    self._player.GetLoan(2)
    self.assertTrue(
        self._player.GetResource().Equal(
            resource.Resource(franc=8, fish=1, loan=2)))
    self._player.ReturnLoan(1)
    self.assertTrue(
        self._player.GetResource().Equal(
            resource.Resource(franc=3, fish=1, loan=1)))


class TestPlayerWorker(unittest.TestCase):
  def setUp(self):
    self._name = 'Player1'
    self._player = player.Player(self._name)

  def testWorkerPlace(self):
    self._player.SetWorkerPlace('building1')
    self.assertEqual(self._player.GetWorkerPlace(), 'building1')


if __name__ == '__main__':
  unittest.main()
