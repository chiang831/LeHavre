import resource

class Player(object):
  def __init__(self, name):
    self._name = name
    self._resource = resource.Resource()

  def GetName(self):
    return self._name

  def GetResource(self):
    return self._resource

  def AddResource(self, add_resource):
    self._resource.Add(add_resource)

  def SubtractResource(self, sub_resource):
    self._resource.Subtract(sub_resource)

