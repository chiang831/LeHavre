"""Module to create building"""

import imp
import os

from game.buildings import building_names

class CreateBuildingError(Exception):
  pass

def _GetModuleName(building_name):
  if building_name not in building_names.MODULE_NAME_DICT:
    raise CreateBuildingError('Can not find building name %s' % building_name)
  return building_names.MODULE_NAME_DICT[building_name]

def CreateBuildingByName(building_name):
  module_name = _GetModuleName(building_name)
  file_path = os.path.join('game', 'buildings', module_name + '.py')
  try:
    module = imp.load_source(building_name, file_path)
  except IOError:
    raise CreateBuildingError(
        'Can not find module %s at %s' % (building_name, file_path))
          
  if not hasattr(module, building_name):
    raise CreateBuildingError('Can not find building class %s' % building_name)
  building_type = getattr(module, building_name)
  return building_type()
