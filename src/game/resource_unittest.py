#!/python
import resource
import unittest

class TestResource(unittest.TestCase):
  def _InitResource(self, **kwargs):
    self._res = resource.Resource(**kwargs)

  def testCreateResourceFromDict(self):
    test_dict = dict(franc=1, wood=2)
    self._res = resource.CreateResourceFromDict(test_dict)
    self.assertEqual(self._res.GetFranc(), test_dict['franc'])
    self.assertEqual(self._res.GetWood(), test_dict['wood'])

  def testResourceInit(self):
    self._InitResource()
    self.assertTrue(self._res)

  def testGetNonZeroResourceNumberDict(self):
    test_dict = dict(franc=1, wood=2)
    self._InitResource(**test_dict)
    self.assertEqual(self._res.GetNonZeroResourceNumberDict(), test_dict)

  def testEqual(self):
    test_dict = dict(franc=1, wood=2)
    self._InitResource(**test_dict)
    res_other = resource.Resource(**test_dict)
    self.assertTrue(self._res.Equal(res_other))

  def testAdd(self):
    dict_1 = dict(franc=1, wood=2)
    dict_2 = dict(franc=1, clay=3)
    dict_sum = dict(franc=2, wood=2, clay=3)
    res_1 = resource.Resource(**dict_1)
    res_2 = resource.Resource(**dict_2)
    res_sum = resource.Resource(**dict_sum)

    res_1.Add(res_2)
    self.assertTrue(res_sum.Equal(res_1))

  def testAddNegativeResource(self):
    dict_1 = dict(franc=1, wood=2)
    dict_2 = dict(franc=1, clay=-3)
    res_1 = resource.Resource(**dict_1)
    res_2 = resource.Resource(**dict_2)

    with self.assertRaises(resource.ResourceError):
      res_1.Add(res_2)

  def testCopy(self):
    dict_1 = dict(franc=1, wood=2)
    res_1 = resource.Resource(**dict_1)
    res_2 = res_1.Copy()
    self.assertTrue(res_1.Equal(res_2))
    self.assertNotEqual(res_1, res_2)

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

if __name__ == '__main__':
  unittest.main()
