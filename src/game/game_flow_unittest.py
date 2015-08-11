"""Unittest for game_flow module."""

import unittest

import config
import game_flow
import game_setting
import resource
import resource_generator
import player

class TestGameFlow(unittest.TestCase):
  def setUp(self):
    self._flow = None
    self._number_of_players = None

  def _CreateGameFlow(self):
    setting = game_setting.GameSetting(self._number_of_players)
    self._flow = game_flow.CreateGameFlow(setting)

  def _CreateAndAddPlayer(self, name):
    player1 = player.Player(name)
    self._flow.AddPlayer(player1)
    return player1

  def testGameFlowStartingResourcePile(self):
    self._number_of_players = 1
    self._CreateGameFlow()
    expected_resource_pile = resource.CreateResourceFromDict(
        config.START_RESOURCES_PILES)
    self.assertTrue(
        self._flow.GetResourcePile().Equal(expected_resource_pile))

  def testGameFlowAddPlayer(self):
    self._number_of_players = 1
    self._CreateGameFlow()
    name = 'Player1'
    self._CreateAndAddPlayer(name)
    self.assertEqual(name, self._flow.GetPlayer(name).GetName())

  def testGameStartingOffer(self):
    self._number_of_players = 2
    self._CreateGameFlow()
    name1 = 'Player1'
    name2 = 'Player2'
    player1 = self._CreateAndAddPlayer(name1)
    player2 = self._CreateAndAddPlayer(name2)
    self._flow.StartingOffer()
    expected_resource = resource.CreateResourceFromDict(
        config.LONG_GAME_STARTING_OFFER)
    self.assertTrue(player1.GetResource().Equal(expected_resource))
    self.assertTrue(player2.GetResource().Equal(expected_resource))

  @classmethod
  def _GetResourceGenerators(cls, res_list):
    res_generator_list = list()
    for res in res_list:
      res_generator_list.append(
          resource_generator.ResourceGenerator(res))
    return res_generator_list

  @classmethod
  def _GetGenerateResourceList(cls):
    resource_generator_dicts = config.RESOURCE_GENERATOR_DICTS
    generate_res_list = list()
    for res_gen_dict in resource_generator_dicts:
      res = resource.CreateResourceFromDict(res_gen_dict)
      generate_res_list.append(res)
    return generate_res_list

  def testResourceGenerator(self):
    self._number_of_players = 1
    self._CreateGameFlow()
    generate_res_list = self._GetGenerateResourceList()
    res_generator_list = self._GetResourceGenerators(generate_res_list)
    self._flow.SetResourceGenerators(res_generator_list)

    expected_res_pile = self._flow.GetResourcePile().Copy()
    for turn in xrange(len(generate_res_list)):
      expected_res_pile.Add(generate_res_list[turn])

      self._flow.GenerateResource()
      self.assertTrue(
          self._flow.GetResourcePile().Equal(expected_res_pile))

      self._flow.NextTurn()

  def testTakeResource(self):
    self._number_of_players = 1
    self._CreateGameFlow()
    res_pile = resource.Resource(franc=1, clay=2)
    name = 'Player1'
    player1 = self._CreateAndAddPlayer(name)
    self._flow.SetResourcePileForTest(res_pile)
    self._flow.PlayerTakeResourceAction('franc')
    self.assertTrue(player1.GetResource().Equal(
        resource.Resource(franc=1)))

  def testGetCurrentPlayer(self):
    self._number_of_players = 2
    self._CreateGameFlow()
    name1 = 'Player1'
    name2 = 'Player2'
    player1 = self._CreateAndAddPlayer(name1)
    player2 = self._CreateAndAddPlayer(name2)
    self.assertEqual(self._flow.GetCurrentPlayer(), player1)
    self._flow.NextTurn()
    self.assertEqual(self._flow.GetCurrentPlayer(), player2)


if __name__ == '__main__':
  unittest.main()
