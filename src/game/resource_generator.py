"""This module handles resource generation in each turn."""

# pylint: disable=R0903
class ResourceGenerator(object):
  def __init__(self, resource):
    self._resource = resource

  def GetResource(self):
    return self._resource
