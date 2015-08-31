"""Unittest for simple_resource_generator_viewer."""

import unittest

import resource
import resource_generator
import simple_resource_generator_viewer as gen_viewer

class TestResourceGeneratorViewer(unittest.TestCase):
  def setUp(self):
    self._viewer = None
    self._generators = None
    self._res_list = None
    self._res1 = None
    self._res2 = None
    self._gen1 = None
    self._gen2 = None

  def _CreateTestGenerators(self):
    self._res1 = resource.Resource(franc=1, fish=1)
    self._res2 = resource.Resource(iron=1, franc=1)
    self._res_list = [self._res1, self._res2]
    self._gen1 = resource_generator.ResourceGenerator(self._res1)
    self._gen2 = resource_generator.ResourceGenerator(self._res2)
    self._generators = [self._gen1, self._gen2]

  def _CreateViewer(self):
    self._viewer = gen_viewer.SimpleResourceGeneratorsViewer(
        self._generators)

  def testViewResourceGenerator(self):
    self._CreateTestGenerators()
    self._CreateViewer()
    self._gen1.SetVisible()
    self._gen2.SetVisible()
    expected_output = 'Generate:'
    expected_output += ' [Fish, Franc]'
    expected_output += ' [Franc, Iron]'
    self.assertEqual(self._viewer.Show(), expected_output)

  def testViewResourceGeneratorInvisible(self):
    self._CreateTestGenerators()
    self._CreateViewer()
    self._gen1.SetVisible()
    expected_output = 'Generate:'
    expected_output += ' [Fish, Franc]'
    expected_output += ' [ Unknown ]'
    self.assertEqual(self._viewer.Show(), expected_output)


if __name__ == '__main__':
  unittest.main()
