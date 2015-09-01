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
    self._players = None
    self._generate_res_list = None

  def _CreateGameFlow(self):
    self._game_setting = game_setting.GameSetting(self._number_of_players)
    self._flow = game_flow.CreateGameFlow(self._game_setting)

  def _CreateAndSetPlayers(self):
    self._players = list()
    for index in xrange(self._number_of_players):
      name = 'Player' + str(index + 1)
      player_obj = player.Player(name)
      self._players.append(player_obj)

    self._flow.SetPlayers(self._players)

  def testGameFlowStartingResourcePile(self):
    self._number_of_players = 1
    self._CreateGameFlow()
    expected_resource_pile = resource.CreateResourceFromDict(
        config.START_RESOURCES_PILES)
    self.assertTrue(
        self._flow.GetResourcePile().Equal(expected_resource_pile))

  def testGameFlowSetPlayers(self):
    self._number_of_players = 2
    self._CreateGameFlow()
    self._CreateAndSetPlayers()
    player1 = self._players[0]
    player2 = self._players[1]
    self.assertEqual(player1, self._flow.GetPlayer(player1.GetName()))
    self.assertEqual(player2, self._flow.GetPlayer(player2.GetName()))

  def testGameStartingOffer(self):
    self._number_of_players = 2
    self._CreateGameFlow()
    self._CreateAndSetPlayers()
    player1 = self._players[0]
    player2 = self._players[1]
    self._SetGenerator()
    self._StartGame()
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
    self._CreateAndSetPlayers()
    self._SetGenerator()
    expected_res_pile = self._flow.GetResourcePile()
    self._StartGame()

    for turn in xrange(self._game_setting.GetNumberOfTurns()):
      expected_res_pile.Add(self._generate_res_list[turn])

      self.assertTrue(
          self._flow.GetResourcePile().Equal(expected_res_pile))

      self._flow.PlayerTakeDummyActionForTest()
      self._flow.NextTurn()

  def testTakeResource(self):
    self._number_of_players = 1
    self._CreateGameFlow()
    res_pile = resource.Resource(franc=1, clay=2)
    self._CreateAndSetPlayers()
    player1 = self._players[0]
    self._SetGenerator()
    self._StartGame()
    self._flow.SetResourcePileForTest(res_pile)
    expected_resource = player1.GetResource().Copy()
    self._flow.PlayerTakeResourceAction('franc')
    expected_resource.Add(resource.Resource(franc=1))
    self.assertTrue(player1.GetResource().Equal(expected_resource))

  def testCanNotTakeResourceInEndOfRound(self):
    self._number_of_players = 1
    self._CreateGameFlow()
    self._CreateAndSetPlayers()
    self._SetGenerator()
    self._StartGame()
    self._PlayOneRound()
    with self.assertRaises(game_flow.GameFlowError):
      self._flow.PlayerTakeResourceAction('franc')

  def testGetCurrentPlayer(self):
    self._number_of_players = 2
    self._CreateGameFlow()
    self._CreateAndSetPlayers()
    player1 = self._players[0]
    player2 = self._players[1]
    self._SetGenerator()
    self._StartGame()
    self.assertEqual(self._flow.GetCurrentPlayer(), player1)
    self._flow.PlayerTakeDummyActionForTest()
    self._flow.NextTurn()
    self.assertEqual(self._flow.GetCurrentPlayer(), player2)

  def _StartGame(self):
    self._flow.StartGame()

  def _PlayOneRound(self):
    for _ in xrange(self._game_setting.GetNumberOfTurns()):
      self._flow.PlayerTakeDummyActionForTest()
      self._flow.NextTurn()

  def testNotFeedYet(self):
    self._number_of_players = 1
    self._CreateGameFlow()
    self._CreateAndSetPlayers()
    player1 = self._players[0]
    player1.AddResource(resource.Resource(franc=2, fish=3))
    self._SetGenerator()
    self._StartGame()
    self._PlayOneRound()

    # Has not pick resource and not call FeedWithPickedForPlayer yet.
    with self.assertRaises(game_flow.GameFlowError):
      self._flow.NextRound()

    # Has not finish feed yet.
    with self.assertRaises(game_flow.GameFlowError):
      self._flow.NextTurn()

  def testFeed(self):
    self._number_of_players = 1
    self._CreateGameFlow()
    self._CreateAndSetPlayers()
    player1 = self._players[0]
    name1 = player1.GetName()
    player1.AddResource(resource.Resource(franc=2, fish=3))
    self._SetGenerator()
    self._StartGame()
    self._PlayOneRound()

    # Let player1 feed for end of round food.
    picker = self._flow.GetFeederForPlayer(name1).GetResourcePicker()
    picker.Pick(franc=2, fish=3)
    self._flow.FeedWithPickedForPlayer(name1)

    # Can enter next round
    self._flow.NextRound()

  def testNotYetNextRound(self):
    self._number_of_players = 1
    self._CreateGameFlow()
    self._CreateAndSetPlayers()
    self._SetGenerator()
    self._StartGame()

    # Can not enter next round
    with self.assertRaises(game_flow.GameFlowError):
      self._flow.NextRound()

  def testGetCurrentTurn(self):
    self._number_of_players = 1
    self._CreateGameFlow()
    self._CreateAndSetPlayers()
    self._SetGenerator()
    self._StartGame()
    self.assertEqual(self._flow.GetCurrentTurn(), 0)
    self._flow.PlayerTakeDummyActionForTest()
    self._flow.NextTurn()
    self.assertEqual(self._flow.GetCurrentTurn(), 1)

  def testGetCurrentRound(self):
    self._number_of_players = 1
    self._CreateGameFlow()
    self._CreateAndSetPlayers()
    player1 = self._players[0]
    name1 = player1.GetName()
    self._SetGenerator()
    self._StartGame()
    self.assertEqual(self._flow.GetCurrentRound(), 0)

    # Let player1 get enough resource in the first round.
    player1.AddResource(resource.Resource(franc=2, fish=3))
    self._PlayOneRound()

    # Let player1 feed for end of round food.
    picker = self._flow.GetFeederForPlayer(name1).GetResourcePicker()
    picker.Pick(franc=2, fish=3)
    self._flow.FeedWithPickedForPlayer(name1)
    self._flow.NextRound()

    self.assertEqual(self._flow.GetCurrentRound(), 1)

  def testGetGameState(self):
    self._number_of_players = 1
    self._CreateGameFlow()
    self.assertEqual(
        self._flow.GetGameState(), game_flow.GameState.PENDING_ADD_PLAYERS)

    self._CreateAndSetPlayers()
    player1 = self._players[0]
    name1 = player1.GetName()
    self.assertEqual(
        self._flow.GetGameState(),
        game_flow.GameState.PENDING_SET_RESOURCE_GENERATORS)

    self._SetGenerator()
    self.assertEqual(
        self._flow.GetGameState(), game_flow.GameState.PENDING_START_GAME)

    self._StartGame()
    self.assertEqual(
        self._flow.GetGameState(), game_flow.GameState.PENDING_USER_ACTION)

    self._flow.PlayerTakeDummyActionForTest()
    self.assertEqual(
        self._flow.GetGameState(), game_flow.GameState.PENDING_USER_DONE)

    self._flow.NextTurn()

    # Let player1 get enough resource in the first round.
    player1.AddResource(resource.Resource(franc=2, fish=3))

    for _ in xrange(6):
      self._flow.PlayerTakeDummyActionForTest()
      self._flow.NextTurn()

    self.assertEqual(
        self._flow.GetGameState(), game_flow.GameState.PENDING_FEEDING)

    # Let player1 feed for end of round food.
    picker = self._flow.GetFeederForPlayer(name1).GetResourcePicker()
    picker.Pick(franc=2, fish=3)
    self._flow.FeedWithPickedForPlayer(name1)
    self.assertEqual(
        self._flow.GetGameState(), game_flow.GameState.PENDING_START_NEXT_ROUND)

    self._flow.NextRound()

  def testGeneratorVisible(self):
    self._number_of_players = 1
    self._CreateGameFlow()
    self._CreateAndSetPlayers()
    player1 = self._players[0]
    name1 = player1.GetName()
    self._SetGenerator()

    self._generators = self._flow.GetResourceGenerators()
    self.assertFalse(self._generators[0].IsVisible())
    self._StartGame()
    for turn in xrange(7):
      self.assertTrue(self._generators[turn].IsVisible())
      self._flow.PlayerTakeDummyActionForTest()
      self._flow.NextTurn()


if __name__ == '__main__':
  unittest.main()
