class ResourceGenerator(object):
  def __init__(self, resource):
    self._resource = resource

  def GetResource(self):
    return self._resource
