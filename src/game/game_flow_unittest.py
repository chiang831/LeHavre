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
    self._game_setting = None
    self._generate_res_list = None

  def _CreateGameFlow(self):
    self._game_setting = game_setting.GameSetting(self._number_of_players)
    self._flow = game_flow.CreateGameFlow(self._game_setting)

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

  def _SetGenerator(self):
    self._generate_res_list = self._GetGenerateResourceList()
    res_generator_list = self._GetResourceGenerators(self._generate_res_list)
    self._flow.SetResourceGenerators(res_generator_list)

  def testResourceGenerator(self):
    self._number_of_players = 1
    self._CreateGameFlow()
    self._SetGenerator()

    expected_res_pile = self._flow.GetResourcePile().Copy()
    for turn in xrange(self._game_setting.GetNumberOfTurns()):
      expected_res_pile.Add(self._generate_res_list[turn])

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

  def _PlayOneRound(self):
    for _ in xrange(self._game_setting.GetNumberOfTurns()):
      self._flow.NextTurn()

  def testNotFeedYet(self):
    name1 = 'Player1'
    self._number_of_players = 1
    self._CreateGameFlow()
    player1 = self._CreateAndAddPlayer(name1)
    player1.AddResource(resource.Resource(franc=2, fish=3))
    self._SetGenerator()
    self._PlayOneRound()

    # Has not pick resource and not call FeedWithPickedForPlayer yet.
    with self.assertRaises(game_flow.GameFlowError):
      self._flow.NextRound()

  def testFeed(self):
    name1 = 'Player1'
    self._number_of_players = 1
    self._CreateGameFlow()
    player1 = self._CreateAndAddPlayer(name1)
    player1.AddResource(resource.Resource(franc=2, fish=3))
    self._SetGenerator()
    self._PlayOneRound()

    # Let player1 feed for end of round food.
    picker = self._flow.GetResourcePickerForPlayer(name1)
    picker.Pick(franc=2, fish=3)
    self._flow.FeedWithPickedForPlayer(name1)

    # Can enter next round
    self._flow.NextRound()

if __name__ == '__main__':
  unittest.main()
