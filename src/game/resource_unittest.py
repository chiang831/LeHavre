#!/python
import resource
import unittest

class TestResource(unittest.TestCase):
  def _InitResource(self, **kwargs):
    self._res = resource.Resource(**kwargs)

  def testCreateResourceFromDict(self):
    test_dict = dict(franc=1, wood=2)
    self._res = resource.CreateResourceFromDict(test_dict)
    self.assertEqual(
        self._res.GetResourceNumberByName('franc'), test_dict['franc'])
    self.assertEqual(
        self._res.GetResourceNumberByName('wood'), test_dict['wood'])

  def testResourceInit(self):
    self._InitResource()
    self.assertTrue(self._res)

  def testGetNonZeroResourceNumberDict(self):
    test_dict = dict(franc=1, wood=2)
    self._InitResource(**test_dict)
    self.assertEqual(self._res.GetNonZeroResourceNumberDict(), test_dict)

  def testGetNonZeroResourceElementDict(self):
    test_dict = dict(franc=1, wood=2)
    self._InitResource(**test_dict)
    res_element_dict = self._res.GetNonZeroResourceElementDict()
    self.assertTrue(isinstance(res_element_dict['franc'], resource.Franc))
    self.assertEqual(res_element_dict['franc'].GetNumber(), 1)
    self.assertTrue(isinstance(res_element_dict['wood'], resource.Wood))
    self.assertEqual(res_element_dict['wood'].GetNumber(), 2)

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

    with self.assertRaises(resource.AddError):
      res_1.Add(res_2)

  def testSubtract(self):
    dict_1 = dict(franc=3, clay=4)
    dict_2 = dict(franc=1, clay=3)
    dict_sub = dict(franc=2, clay=1)
    res_1 = resource.Resource(**dict_1)
    res_2 = resource.Resource(**dict_2)
    res_sub = resource.Resource(**dict_sub)

    res_1.Subtract(res_2)
    self.assertTrue(res_sub.Equal(res_1))

  def testSubtractInvalid(self):
    dict_1 = dict(franc=3, clay=3)
    dict_2 = dict(franc=1, clay=4)
    res_1 = resource.Resource(**dict_1)
    res_2 = resource.Resource(**dict_2)
    with self.assertRaises(resource.SubtractionError):
      res_1.Subtract(res_2)

  def testCopy(self):
    dict_1 = dict(franc=1, wood=2)
    res_1 = resource.Resource(**dict_1)
    res_2 = res_1.Copy()
    self.assertTrue(res_1.Equal(res_2))
    self.assertNotEqual(res_1, res_2)


class TestGetResource(unittest.TestCase):
  def setUp(self):
    self._name = None
    self._value = 1

  def _InitResource(self):
    self._res = resource.CreateResourceFromDict(
        {self._name: self._value})

  def _TestGetResource(self):
    self._InitResource()
    self.assertEqual(
        self._res.GetResourceNumberByName(self._name),
        self._value)

  def testGetFranc(self):
    self._name = 'franc'
    self._TestGetResource()

  def testGetFish(self):
    self._name = 'fish'
    self._TestGetResource()

  def testGetWood(self):
    self._name = 'wood'
    self._TestGetResource()

  def testGetClay(self):
    self._name = 'clay'
    self._TestGetResource()

  def testGetIron(self):
    self._name = 'iron'
    self._TestGetResource()

  def testGetGrain(self):
    self._name = 'grain'
    self._TestGetResource()

  def testGetCattle(self):
    self._name = 'cattle'
    self._TestGetResource()

  def testGetCoal(self):
    self._name = 'coal'
    self._TestGetResource()

  def testGetHides(self):
    self._name = 'hides'
    self._TestGetResource()

  def testGetSmokedFish(self):
    self._name = 'smoked_fish'
    self._TestGetResource()

  def testGetCharcoal(self):
    self._name = 'charcoal'
    self._TestGetResource()

  def testGetBrick(self):
    self._name = 'brick'
    self._TestGetResource()

  def testGetSteel(self):
    self._name = 'steel'
    self._TestGetResource()

  def testGetBread(self):
    self._name = 'bread'
    self._TestGetResource()

  def testGetMeal(self):
    self._name = 'meal'
    self._TestGetResource()

  def testGetLeather(self):
    self._name = 'leather'
    self._TestGetResource()

  def testGetCoke(self):
    self._name = 'coke'
    self._TestGetResource()

  def testGetLoan(self):
    self._name = 'loan'
    self._TestGetResource()

  def _TestClearResource(self):
    self._InitResource()
    self._res.ClearResourceByName(self._name)
    self.assertEqual(
        self._res.GetResourceNumberByName(self._name),
        0)

  def testClearFranc(self):
    self._name = 'franc'
    self._TestClearResource()

  def testClearWood(self):
    self._name = 'wood'
    self._TestClearResource()

  def testClearClay(self):
    self._name = 'clay'
    self._TestClearResource()

  def testClearFish(self):
    self._name = 'fish'
    self._TestClearResource()

  def testClearIron(self):
    self._name = 'iron'
    self._TestClearResource()

  def testClearGrain(self):
    self._name = 'grain'
    self._TestClearResource()

  def testClearCattle(self):
    self._name = 'cattle'
    self._TestClearResource()

  def testClearSmokedFish(self):
    self._name = 'smoked_fish'
    self._TestClearResource()

  def testClearCharcoal(self):
    self._name = 'charcoal'
    self._TestClearResource()

  def testClearBrick(self):
    self._name = 'brick'
    self._TestClearResource()

  def testClearSteel(self):
    self._name = 'steel'
    self._TestClearResource()

  def testClearCoke(self):
    self._name = 'coke'
    self._TestClearResource()

  def testClearBread(self):
    self._name = 'bread'
    self._TestClearResource()

  def testClearMeal(self):
    self._name = 'meal'
    self._TestClearResource()

  def testClearLeather(self):
    self._name = 'leather'
    self._TestClearResource()

  def testClearLoan(self):
    self._name = 'loan'
    self._TestClearResource()


class TestGetFoodValue(unittest.TestCase):
  def testFranc(self):
    res = resource.Resource(franc=1)
    self.assertEqual(res.GetFoodValue(), 1)

  def testFish(self):
    res = resource.Resource(fish=1)
    self.assertEqual(res.GetFoodValue(), 1)

  def testFrandAndFish(self):
    res = resource.Resource(franc=1, fish=1)
    self.assertEqual(res.GetFoodValue(), 2)

  def testNonFood(self):
    res = resource.Resource(wood=1, clay=1, iron=1, grain=1, cattle=1)
    self.assertEqual(res.GetFoodValue(), 0)

  def testSmokedFish(self):
    res = resource.Resource(smoked_fish=1)
    self.assertEqual(res.GetFoodValue(), 2)

  def testBread(self):
    res = resource.Resource(bread=1)
    self.assertEqual(res.GetFoodValue(), 2)

  def testMeal(self):
    res = resource.Resource(meal=1)
    self.assertEqual(res.GetFoodValue(), 3)


class TestBasicResourceElement(unittest.TestCase):
  def testGetNumber(self):
    element = resource.Franc(1)
    self.assertEqual(element.GetNumber(), 1)

  def testAdd(self):
    element = resource.Franc(1)
    element.Add(1)
    self.assertEqual(element.GetNumber(), 2)

  def testSubtract(self):
    element = resource.Franc(1)
    element.Subtract(1)
    self.assertEqual(element.GetNumber(), 0)

  def testSubtractInvalid(self):
    element = resource.Franc(1)
    with self.assertRaises(resource.SubtractionError):
      element.Subtract(2)

  def testGetFoodValueFranc(self):
    element = resource.Franc(1)
    self.assertEqual(element.GetFoodValue(), 1)

  def testGetUnitFoodValueFranc(self):
    element = resource.Franc(0)
    self.assertEqual(element.GetUnitFoodValue(), 1)

  def testGetFoodValueFish(self):
    element = resource.Fish(1)
    self.assertEqual(element.GetFoodValue(), 1)

  def testGetUnitFoodValueFish(self):
    element = resource.Fish(0)
    self.assertEqual(element.GetUnitFoodValue(), 1)


class TestGetLoanValue(unittest.TestCase):
  def testLoanGet(self):
    self.assertEqual(resource.Loan.GetFrancValueWhenGetLoan(), 4)

  def testLoanReturn(self):
    self.assertEqual(resource.Loan.GetFrancValueWhenReturnLoan(), 5)


if __name__ == '__main__':
  unittest.main()
