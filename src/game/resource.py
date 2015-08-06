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

  def GetNonZeroResourceNumberDict(self):
    ret = dict()
    for key, value in self._resource_dict.iteritems():
      number = self._GetResourceNumber(key)
      if number:
        ret[key] = number     
    return ret

  def _GetResourceNumber(self, name):
    return self._resource_dict[name]._number

  def GetFranc(self):
    return self._GetResourceNumber('franc')

  def GetFish(self):
    return self._GetResourceNumber('fish')

  def GetWood(self):
    return self._GetResourceNumber('wood')

  def GetClay(self):
    return self._GetResourceNumber('clay')

  def GetIron(self):
    return self._GetResourceNumber('iron')

  def GetGrain(self):
    return self._GetResourceNumber('grain')

  def GetCattle(self):
    return self._GetResourceNumber('cattle')

  def GetCoal(self):
    return self._GetResourceNumber('coal')

  def GetHides(self):
    return self._GetResourceNumber('hides')


def CreateResourceFromDict(resource_dict):
  return Resource(**resource_dict)


class BasicResourceType(object):
  def __init__(self, number):
    self._number = number
 
  def GetNumber(self):
    return self._number 

  def Add(self, number):
    self._number = self._number + number


class Franc(BasicResourceType):
  name = 'Franc'  
  def __init__(self, number):
    super(Franc, self).__init__(number)


class Fish(BasicResourceType):
  name = 'Fish' 
  def __init__(self, number):
    super(Fish, self).__init__(number)


class Wood(BasicResourceType):
  name = 'Wood' 
  def __init__(self, number):
    super(Wood, self).__init__(number)


class Clay(BasicResourceType):
  name = 'Clay' 
  def __init__(self, number):
    super(Clay, self).__init__(number)


class Iron(BasicResourceType):
  name = 'Iron' 
  def __init__(self, number):
    super(Iron, self).__init__(number)


class Grain(BasicResourceType):
  name = 'Grain' 
  def __init__(self, number):
    super(Grain, self).__init__(number)


class Cattle(BasicResourceType):
  name = 'Cattle' 
  def __init__(self, number):
    super(Cattle, self).__init__(number)


class Coal(BasicResourceType):
  name = 'Coal' 
  def __init__(self, number):
    super(Coal, self).__init__(number)


class Hides(BasicResourceType):
  name = 'Hides' 
  def __init__(self, number):
    super(Hides, self).__init__(number)
