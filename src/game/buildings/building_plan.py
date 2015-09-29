"""Module for building plans."""

class BuildingPlanError(Exception):
  pass

class BuildingPlan(object):
  def __init__(self, queues):
    self._queues = queues

  def GetPlans(self):
    plans = []
    for index in xrange(3):
      if self._queues[index]:
        plans.append(self._queues[index][0])
    return plans

  def Remove(self, name):
    find_index = None
    for index in xrange(3):
      if not self._queues[index]:
        continue
      if self._queues[index][0].GetName() == name:
        find_index = index
        break
    if find_index is None:
      raise BuildingPlanError('Can not find building %s from plans' % name)
    self._queues[find_index].pop(0)

  def GetAllPlans(self):
    return self._queues
