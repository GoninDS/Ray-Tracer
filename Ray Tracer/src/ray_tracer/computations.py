# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

class Computation():
  # Default constructor
  def __init__(self):
    self.t = 0
    self.inside = False
    self.object = None
    self.point = None
    self.eyev = None
    self.normalv = None

  # Debugging representation
  def __repr__(self):
    return 'Computation()'
  
  # String representation
  def __str__(self): 
    return '({}, {}, {}, {}, {})'.format( \
      self.t, self.object, self.point, self.eyev, self.normalv)
  
  # Returns a computations object
  @staticmethod
  def prepare_computations(intersection, ray):
    # Create a computations object
    comps = Computation()
    # Get the t and the object from the intersection
    comps.t = intersection.t
    comps.object = intersection.object
    # Calculate the point, eye vector and normal vector
    comps.point = ray.position(comps.t)
    comps.eyev = -ray.direction
    comps.normalv = comps.object.normal_at(comps.point)
    # If the dot product between the normal and the eye vector
    # is less than 0
    if comps.normalv.dot(comps.eyev) < 0:
      # The ray is inside the object and the normal should be reversed
      comps.inside = True
      comps.normalv = -comps.normalv
    # Otherwise
    else:
      # The ray isnt inside the object
      comps.inside = False
    # Return the computations object
    return comps

  # Returns the hit from a list of intersections
  @staticmethod
  def hit(intersections):
    min = None
    for intersection in intersections:
      if (min is None or abs(intersection.t) < min.t):
        min = intersection
    return min
  
  # Calculates the color taking into account the light
  def shade_hit(self, light):
    return light.lighting(self.object.material, self.point,
      self.eyev, self.normalv)

  # TODO(Luis & Kenneth): Implement this
  # TODO(Kenneth): Idk if we should have this here
  @staticmethod
  def color_at(world, ray):
    pass