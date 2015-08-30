"""Unittest for simple_player_viewer."""

import unittest

import player
import resource
import simple_player_viewer
import simple_resource_viewer

class TestPlayerViewer(unittest.TestCase):
  def setUp(self):
    self._name = None
    self._res = None
    self._player = None
    self._expected_output = None

  def _CreateTestPlayer(self):
    self._name = 'Player1'
    self._res = resource.Resource(franc=1, fish=2)
    self._player = player.Player(self._name)
    self._player.AddResource(self._res)

  def _SetExpectedOutput(self):
    self._expected_output = 'Player: %s\n' % self._name
    res_viewer = simple_resource_viewer.SimpleResourceViewer()
    res_viewer.SetResource(self._res)
    self._expected_output += res_viewer.Show()

  def testPlayerViewer(self):
    self._CreateTestPlayer()
    self._SetExpectedOutput()
    player_viewer = simple_player_viewer.SimplePlayerViewer(self._player)
    self.assertEqual(self._expected_output, player_viewer.Show())

  def testShowPlayer(self):
    self._CreateTestPlayer()
    self._SetExpectedOutput()
    self.assertEqual(
        self._expected_output,
        simple_player_viewer.ShowPlayer(self._player))


if __name__ == '__main__':
  unittest.main()
