"""This module provides simple viewer for game flow."""


class SimpleFlowViewer(object):
  def __init__(self, flow):
    self._flow = flow 

  def Show(self):
    game_state = self._flow.GetGameState()
    output = 'Game State: %s\n' % game_state

    current_round = self._flow.GetCurrentRound() + 1
    current_turn = self._flow.GetCurrentTurn() + 1
    food = self._flow.GetThisRoundFoodRequirement()

    output += ('Round: %d    Turn: %d    Food Requirement: %d\n' %
               (current_round, current_turn, food))

    output += 'Current player: %s\n' % self._flow.GetCurrentPlayer().GetName()


    return output


def ShowFlow(flow_obj):
  viewer = SimpleFlowViewer(flow_obj)
  return viewer.Show()
