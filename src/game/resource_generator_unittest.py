import unittest

import resource
import resource_generator

class TestResourceGenerator(unittest.TestCase):
  def testGetResource(self):
    res_dict = dict(franc=1, wood=1)
    res = resource.CreateResourceFromDict(res_dict)
    generator = resource_generator.ResourceGenerator(res)
    self.assertTrue(generator.GetResource().Equal(res))

if __name__ == '__main__':
  unittest.main()
