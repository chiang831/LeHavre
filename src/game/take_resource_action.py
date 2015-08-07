import resource

class TakeResourceActionError(Exception):
  pass


class TakeResourceAction(object):
  _name = None

  def TakeAction(self, player, resource_pile):
    res_to_take = self._GetResourceToTake(resource_pile)
    self._CheckResourceToTake(res_to_take)
    self._ClearResourceToTake(resource_pile)
    player.AddResource(res_to_take)

  def _GetResourceToTake(self, resource_pile):
    return resource.CreateResourceFromDict(
        {self._name: resource_pile.GetResourceByName(self._name)})

  def _CheckResourceToTake(self, res):
    if self._GetNumberOfResourceToTake(res) <= 0: 
      raise TakeResourceActionError('No resource to take')

  def _GetNumberOfResourceToTake(self, res):
    return res.GetResourceByName(self._name)

  def _ClearResourceToTake(self, resource_pile):
    resource_pile.ClearResourceByName(self._name)


class TakeFrancAction(TakeResourceAction):
  _name = 'franc'

class TakeFishAction(TakeResourceAction):
  _name = 'fish'

class TakeWoodAction(TakeResourceAction):
  _name = 'wood'

class TakeClayAction(TakeResourceAction):
  _name = 'clay'

class TakeIronAction(TakeResourceAction):
  _name = 'iron'

class TakeGrainAction(TakeResourceAction):
  _name = 'grain'

class TakeCattleAction(TakeResourceAction):
  _name = 'cattle'

def CreateTakeResourceAction(name):
  action_dict = {
      'franc': TakeFrancAction,
      'fish': TakeFishAction,
      'wood': TakeWoodAction,
      'clay': TakeClayAction,
      'iron': TakeIronAction,
      'grain': TakeGrainAction,
      'cattle': TakeCattleAction,
  }
  return action_dict[name]()
