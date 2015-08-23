"""Simple resource viewer."""

class SimpleResourceViewer(object):
  def __init__(self):
    self._res = None

  def SetResource(self, res):
    self._res = res

  def Show(self):
    elements = self._res.GetNonZeroResourceElementDict().values()
    output = ''
    for element in elements:
      output += '%s: %d\n' % (element.name, element.GetNumber())
    return output

def ShowResource(res):
  viewer = SimpleResourceViewer()
  viewer.SetResource(res)
  return viewer.Show()
