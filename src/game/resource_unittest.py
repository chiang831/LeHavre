#!/python
import unittest
import resource

class TestResource(unittest.TestCase):
  def _InitResource(self, **kwargs):
    self._res = resource.Resource(**kwargs)

  def testResourceInit(self):
    self._InitResource()
    self.assertTrue(self._res)

  def testGetFranc(self):
    self._InitResource(franc=1) 
    self.assertEqual(self._res.GetFranc(), 1)

  def testGetFish(self):
    self._InitResource(fish=1) 
    self.assertEqual(self._res.GetFish(), 1)

  def testGetWood(self):
    self._InitResource(wood=1) 
    self.assertEqual(self._res.GetWood(), 1)

  def testGetClay(self):
    self._InitResource(clay=1) 
    self.assertEqual(self._res.GetClay(), 1)

  def testGetIron(self):
    self._InitResource(iron=1) 
    self.assertEqual(self._res.GetIron(), 1)

  def testGetGrain(self):
    self._InitResource(grain=1) 
    self.assertEqual(self._res.GetGrain(), 1)

  def testGetCattle(self):
    self._InitResource(cattle=1) 
    self.assertEqual(self._res.GetCattle(), 1)

  def testGetCoal(self):
    self._InitResource(coal=1) 
    self.assertEqual(self._res.GetCoal(), 1)

  def testGetHides(self):
    self._InitResource(hides=1) 
    self.assertEqual(self._res.GetHides(), 1)
