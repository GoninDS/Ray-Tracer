from ray_tracer.shapes import Shape

class Sample_shape(Shape):
  # Default constructor
  def __init__(self, material=None):
    super().__init__(material)

  @staticmethod
  def test_default():
    return Sample_shape()

  # Debugging representation
  def __repr__(self):
    return 'Sample_shape()'
  
  # String representation
  def __str__(self): 
    return '({}, {})'.format(self.transform, self.id)

  # Method to handle the normal implementation for the shape
  def local_normal_at(self, local_point):
    local_point.w = 0
    return local_point

  def local_intersect(self, local_ray):
    return local_ray