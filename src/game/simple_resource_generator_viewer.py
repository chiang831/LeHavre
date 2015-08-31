"""This module provides simple viewer for resource generators."""

class SimpleResourceGeneratorsViewer(object):
  def __init__(self, resource_generators):
    self._generators = resource_generators

  def Show(self):
    output = 'Generate:'
    for gen in self._generators:
      if not gen.IsVisible():
        output += ' [ Unknown ]'
        continue
      elements = gen.GetResource().GetNonZeroResourceElementDict().values()
      element_names = (elements[0].name, elements[1].name)
      sorted_names = sorted(element_names)
      output += ' [%s, %s]' % (sorted_names[0], sorted_names[1])
    return output
