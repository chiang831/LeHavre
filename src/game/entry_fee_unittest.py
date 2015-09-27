"""Unittest for entry fee module."""

import unittest

from game import entry_fee

class TestEntryFee(unittest.TestCase):
  def testEntryFee(self):
    fee = entry_fee.EntryFee(franc=1, food=2)
    self.assertEqual(2, fee.food)
    self.assertEqual(1, fee.franc)

if __name__ == '__main__':
  unittest.main()
