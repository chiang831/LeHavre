"""This module handles resource generation in each turn."""

import config
import random
import resource

# pylint: disable=R0903
class ResourceGenerator(object):
  def __init__(self, res):
    self._resource = res
    self._visible = False

  def GetResource(self):
    return self._resource

  def IsVisible(self):
    return self._visible

  def SetVisible(self):
    self._visible = True


def GetShuffledResourceGenerators():
  res_generator_list = _GetResourceGenerators()
  random.shuffle(res_generator_list)
  return res_generator_list


def _GetResourceGenerators():
  resource_generator_dicts = config.RESOURCE_GENERATOR_DICTS
  res_generator_list = list()
  for res_gen_dict in resource_generator_dicts:
    res = resource.CreateResourceFromDict(res_gen_dict)
    res_gen = ResourceGenerator(res)
    res_generator_list.append(res_gen)
  return res_generator_list
