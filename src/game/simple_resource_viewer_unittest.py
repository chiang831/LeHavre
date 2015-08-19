"""Unittest for simple_resource_viewer."""

import unittest

import resource
import simple_resource_viewer

class TestResourceViewer(unittest.TestCase):
  def testShowResource(self):
    viewer = simple_resource_viewer.SimpleResourceViewer()
    res = resource.Resource(franc=1, fish=2)
    viewer.SetResource(res)
    expected_output = 'Franc: 1\nFish: 2\n'
    self.assertEqual(expected_output, viewer.Show())


if __name__ == '__main__':
  unittest.main()
