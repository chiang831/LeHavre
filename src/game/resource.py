class ResourceError(Exception):
  pass

class Resource(object):
  def __init__(self, franc=0, fish=0, wood=0, clay=0, iron=0, 
               grain=0, cattle=0, coal=0, hides=0):
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
      number = self.GetResourceByName(key)
      if number:
        ret[key] = number     
    return ret

  def GetNonZeroResourceElementDict(self):
    ret = dict()
    for key, value in self._resource_dict.iteritems():
      number = self.GetResourceByName(key)
      if number:
        ret[key] = value
    return ret

  def GetResourceByName(self, name):
    return self._resource_dict[name]._number

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


class Wood(BasicResourceElement):
  name = 'Wood' 
  def __init__(self, number):
    super(Wood, self).__init__(number)


class Clay(BasicResourceElement):
  name = 'Clay' 
  def __init__(self, number):
    super(Clay, self).__init__(number)


class Iron(BasicResourceElement):
  name = 'Iron' 
  def __init__(self, number):
    super(Iron, self).__init__(number)


class Grain(BasicResourceElement):
  name = 'Grain' 
  def __init__(self, number):
    super(Grain, self).__init__(number)


class Cattle(BasicResourceElement):
  name = 'Cattle' 
  def __init__(self, number):
    super(Cattle, self).__init__(number)


class Coal(BasicResourceElement):
  name = 'Coal' 
  def __init__(self, number):
    super(Coal, self).__init__(number)


class Hides(BasicResourceElement):
  name = 'Hides' 
  def __init__(self, number):
    super(Hides, self).__init__(number)


def CreateResourceFromDict(resource_dict):
  return Resource(**resource_dict)


