class ResourceError(Exception):
  pass

class Resource(object):
  def __init__(self, franc=0, fish=0, wood=0, clay=0, iron=0, 
               grain=0, cattle=0, coal=0, hides=0,
               smoked_fish=0, charcoal=0, brick=0, steel=0,
               bread=0, meal=0, coke=0, leather=0):
    self._resource_dict = dict()
    self._resource_dict['franc'] = Franc(franc)
    self._resource_dict['fish'] = Fish(fish)
    self._resource_dict['wood'] = Wood(wood)
    self._resource_dict['clay'] = Clay(clay)
    self._resource_dict['iron'] = Iron(iron)
    self._resource_dict['grain'] = Grain(grain)
    self._resource_dict['cattle'] = Cattle(cattle)
    self._resource_dict['coal'] = Coal(coal)
    self._resource_dict['hides'] = Hides(hides)
    self._resource_dict['smoked_fish'] = SmokedFish(smoked_fish)
    self._resource_dict['charcoal'] = Charcoal(charcoal)
    self._resource_dict['brick'] = Brick(brick)
    self._resource_dict['steel'] = Steel(steel)
    self._resource_dict['bread'] = Bread(bread)
    self._resource_dict['meal'] = Meal(meal)
    self._resource_dict['coke'] = Coke(coke)
    self._resource_dict['leather'] = Leather(leather)

  def Equal(self, other):
    return (self.GetNonZeroResourceNumberDict() == 
            other.GetNonZeroResourceNumberDict())

  def Add(self, other):
    for key, value in other.GetNonZeroResourceNumberDict().iteritems():
      if value < 0:
        raise ResourceError('Can not add a negative %d for key %s',
            value, key)
      self._resource_dict[key].Add(value)

  def Copy(self):
    return CreateResourceFromDict(self.GetNonZeroResourceNumberDict())

  def GetNonZeroResourceNumberDict(self):
    ret = dict()
    for key, value in self._resource_dict.iteritems():
      number = self.GetResourceNumberByName(key)
      if number:
        ret[key] = number     
    return ret

  def GetNonZeroResourceElementDict(self):
    ret = dict()
    for key, value in self._resource_dict.iteritems():
      number = self.GetResourceNumberByName(key)
      if number:
        ret[key] = value
    return ret

  def _GetResourceByName(self, name):
    return self._resource_dict[name]

  def GetResourceNumberByName(self, name):
    return self._GetResourceByName(name).GetNumber()

  def ClearResourceByName(self, name):
    self._resource_dict[name]._number = 0

  def GetFoodValue(self):
    food = 0
    for res_element in self._resource_dict.values():
      if res_element.GetNumber():
        food = food + res_element.GetFoodValue()
    return food


class BasicResourceElement(object):
  _unit_food_value = 0
  def __init__(self, number):
    self._number = number
 
  def GetNumber(self):
    return self._number 

  def Add(self, number):
    self._number = self._number + number

  def GetFoodValue(self):
    return self._unit_food_value * self._number

  def GetUnitFoodValue(self):
    return self._unit_food_value


class Franc(BasicResourceElement):
  name = 'Franc'  
  _unit_food_value = 1
  def __init__(self, number):
    super(Franc, self).__init__(number)


class Fish(BasicResourceElement):
  name = 'Fish' 
  _unit_food_value = 1
  def __init__(self, number):
    super(Fish, self).__init__(number)


class SmokedFish(Fish):
  name = 'Smoked Fish' 
  _unit_food_value = 2
  def __init__(self, number):
    super(SmokedFish, self).__init__(number)


class Wood(BasicResourceElement):
  name = 'Wood' 
  def __init__(self, number):
    super(Wood, self).__init__(number)


class Charcoal(Wood):
  name = 'Charcoal' 
  def __init__(self, number):
    super(Charcoal, self).__init__(number)


class Clay(BasicResourceElement):
  name = 'Clay' 
  def __init__(self, number):
    super(Clay, self).__init__(number)


class Brick(Clay):
  name = 'Brick' 
  def __init__(self, number):
    super(Brick, self).__init__(number)


class Iron(BasicResourceElement):
  name = 'Iron' 
  def __init__(self, number):
    super(Iron, self).__init__(number)


class Steel(Iron):
  name = 'Steel' 
  def __init__(self, number):
    super(Steel, self).__init__(number)


class Grain(BasicResourceElement):
  name = 'Grain' 
  def __init__(self, number):
    super(Grain, self).__init__(number)


class Bread(Grain):
  name = 'Bread' 
  _unit_food_value = 2
  def __init__(self, number):
    super(Bread, self).__init__(number)


class Cattle(BasicResourceElement):
  name = 'Cattle' 
  def __init__(self, number):
    super(Cattle, self).__init__(number)


class Meal(Cattle):
  name = 'Meal' 
  _unit_food_value = 3
  def __init__(self, number):
    super(Cattle, self).__init__(number)


class Coal(BasicResourceElement):
  name = 'Coal' 
  def __init__(self, number):
    super(Coal, self).__init__(number)


class Coke(Coal):
  name = 'Coke' 
  def __init__(self, number):
    super(Coke, self).__init__(number)


class Hides(BasicResourceElement):
  name = 'Hides' 
  def __init__(self, number):
    super(Hides, self).__init__(number)


class Leather(Hides):
  name = 'Leather' 
  def __init__(self, number):
    super(Leather, self).__init__(number)


def CreateResourceFromDict(resource_dict):
  return Resource(**resource_dict)


