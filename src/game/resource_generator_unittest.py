"""Unittest for resource_generator."""

import unittest

from game import config
from game import resource
from game import resource_generator

class TestResourceGenerator(unittest.TestCase):
  def setUp(self):
    self._generator = None
    self._res = None

  def _CreateTestGenerator(self):
    res_dict = dict(franc=1, wood=1)
    self._res = resource.CreateResourceFromDict(res_dict)
    self._generator = resource_generator.ResourceGenerator(self._res)

  def testGetResource(self):
    self._CreateTestGenerator()
    self.assertTrue(self._generator.GetResource().Equal(self._res))

  def testIsVisible(self):
    self._CreateTestGenerator()
    self.assertFalse(self._generator.IsVisible())

  def testSetVisible(self):
    self._CreateTestGenerator()
    self.assertFalse(self._generator.IsVisible())
    self._generator.SetVisible()
    self.assertTrue(self._generator.IsVisible())


class TestGetShuffledResourceGenerators(unittest.TestCase):
  def testGetShuffledResourceGenerators(self):
    # Generate two resource generator lists which shuffles.
    res_gen_list_1 = resource_generator.GetShuffledResourceGenerators()
    res_gen_list_2 = resource_generator.GetShuffledResourceGenerators()
    res_list_1 = list()
    res_list_2 = list()
    self.assertEqual(len(res_gen_list_1), len(res_gen_list_2))

    # Extract the resources from two lists.
    for index in xrange(len(res_gen_list_1)):
      res_list_1.append(res_gen_list_1[index].GetResource())
      res_list_2.append(res_gen_list_2[index].GetResource())

    # Get the golden resource list.
    resource_generator_dicts = config.RESOURCE_GENERATOR_DICTS
    golden_res_list = list()
    for res_gen_dict in resource_generator_dicts:
      res = resource.CreateResourceFromDict(res_gen_dict)
      golden_res_list.append(res)

    # Compare resource generator list 1 and 2.
    for res_1 in res_list_1:
      match = False
      for res_2 in res_list_2:
        if res_1.Equal(res_2):
          match = True
      self.assertTrue(match)

    # Compare resource generator list 1 and golden.
    for res_1 in res_list_1:
      match = False
      for golden in golden_res_list:
        if res_1.Equal(golden):
          match = True
      self.assertTrue(match)


if __name__ == '__main__':
  unittest.main()
