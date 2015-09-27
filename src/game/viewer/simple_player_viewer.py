"""This module provides simple viewer for player."""

from game.viewer import simple_resource_viewer as resource_viewer

class SimplePlayerViewer(object):
  def __init__(self, player):
    self._player = player

  def Show(self):
    output = ''
    output += 'Player: %s\n' % self._player.GetName()
    output += resource_viewer.ShowResource(self._player.GetResource())
    return output

def ShowPlayer(player_obj):
  viewer = SimplePlayerViewer(player_obj)
  return viewer.Show()
