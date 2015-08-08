import unittest

import config
import game_flow
import game_setting
import resource
import resource_generator
import player

class TestGameFlow(unittest.TestCase):
  def setUp(self):
    setting = game_setting.GameSetting()
    self._flow = game_flow.CreateGameFlow(setting) 
    self._generate_res_list = None

  def _CreateAndAddPlayer(self, name):
    p = player.Player(name)
    self._flow.AddPlayer(p)
    return p

  def testGameFlowStartingResourcePile(self):
    expected_resource_pile = resource.CreateResourceFromDict(
        config.START_RESOURCES_PILES)
    self.assertTrue(
        self._flow.GetResourcePile().Equal(expected_resource_pile))

  def testGameFlowAddPlayer(self):
    name = 'Player1'
    self._CreateAndAddPlayer(name)
    self.assertEqual(name, self._flow.GetPlayer(name).GetName())

  def testGameStartingOffer(self):
    name1 = 'Player1'
    name2 = 'Player2'
    p1 = self._CreateAndAddPlayer(name1)
    p2 = self._CreateAndAddPlayer(name2)
    self._flow.StartingOffer()
    expected_resource = resource.CreateResourceFromDict(
        config.LONG_GAME_STARTING_OFFER)
    self.assertTrue(p1.GetResource().Equal(expected_resource))
    self.assertTrue(p2.GetResource().Equal(expected_resource))

  def _SetResourceGenerators(self):
    resource_generator_dicts = config.RESOURCE_GENERATOR_DICTS
    self._generate_res_list = list()
    res_gen_list = list()
    for res_gen_dict in resource_generator_dicts:
      res = resource.CreateResourceFromDict(res_gen_dict)
      self._generate_res_list.append(res)
      res_gen_list.append(
          resource_generator.ResourceGenerator(res))

    self._flow.SetResourceGenerators(res_gen_list)

  def testResourceGenerator(self):
    self._SetResourceGenerators()

    expected_res_pile = self._flow.GetResourcePile().Copy()
    for turn in xrange(len(self._generate_res_list)):
      expected_res_pile.Add(self._generate_res_list[turn])

      self._flow.GenerateResource()
      self.assertTrue(
          self._flow.GetResourcePile().Equal(expected_res_pile))

      self._flow.NextTurn()

  def testTakeResource(self):
    res_pile = resource.Resource(franc=1, clay=2)
    name = 'Player1'
    p1 = self._CreateAndAddPlayer(name)
    self._flow.SetResourcePileForTest(res_pile)
    self._flow.PlayerTakeResourceAction(name, 'franc')
    self.assertTrue(p1.GetResource().Equal(
        resource.Resource(franc=1)))

if __name__ == '__main__':
  unittest.main()
