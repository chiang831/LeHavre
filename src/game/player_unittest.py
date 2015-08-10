import unittest

import player
import resource

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


if __name__ == '__main__':
  unittest.main()
