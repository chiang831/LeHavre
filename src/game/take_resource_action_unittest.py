import unittest

import take_resource_action 
import resource
import player

class TestTakeResourceAction(unittest.TestCase):
  def setUp(self):
    self._res_name = None

  def _testTakeResourceAction(self):
    p = player.Player('Player1')
    p.AddResource(resource.CreateResourceFromDict({self._res_name: 1}))
    resource_pile = resource.CreateResourceFromDict({self._res_name: 2})
    action = take_resource_action.CreateTakeResourceAction(self._res_name)

    action.TakeAction(p, resource_pile)

    self.assertEqual(p.GetResource().GetResourceNumberByName(self._res_name), 3)
    self.assertEqual(resource_pile.GetResourceNumberByName(self._res_name), 0)

  def _testTakeInvalidResourceAction(self):
    p= player.Player('Player1')
    resource_pile = resource.Resource()
    action = take_resource_action.CreateTakeResourceAction(self._res_name)

    with self.assertRaises(
        take_resource_action.TakeResourceActionError):
      action.TakeAction(p, resource_pile)

  def testTakeFrancAction(self):
    self._res_name = 'franc'
    self._testTakeResourceAction()

  def testTakeInvalidFrancAction(self):
    self._res_name = 'franc'
    self._testTakeInvalidResourceAction()

  def testTakeFrancAction(self):
    self._res_name = 'fish'
    self._testTakeResourceAction()

  def testTakeInvalidFishAction(self):
    self._res_name = 'fish'
    self._testTakeInvalidResourceAction()

  def testTakeWoodAction(self):
    self._res_name = 'wood'
    self._testTakeResourceAction()

  def testTakeInvalidWoodAction(self):
    self._res_name = 'wood'
    self._testTakeInvalidResourceAction()

  def testTakeClayAction(self):
    self._res_name = 'clay'
    self._testTakeResourceAction()

  def testTakeInvalidClayAction(self):
    self._res_name = 'clay'
    self._testTakeInvalidResourceAction()

  def testTakeIronAction(self):
    self._res_name = 'iron'
    self._testTakeResourceAction()

  def testTakeInvalidIronAction(self):
    self._res_name = 'iron'
    self._testTakeInvalidResourceAction()

  def testTakeGrainAction(self):
    self._res_name = 'grain'
    self._testTakeResourceAction()

  def testTakeInvalidGrainAction(self):
    self._res_name = 'grain'
    self._testTakeInvalidResourceAction()

  def testTakeCattleAction(self):
    self._res_name = 'cattle'
    self._testTakeResourceAction()

  def testTakeInvalidCattleAction(self):
    self._res_name = 'cattle'
    self._testTakeInvalidResourceAction()

if __name__ == '__main__':
  unittest.main()
