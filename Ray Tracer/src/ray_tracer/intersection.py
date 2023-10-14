# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

from ray_tracer.rays import Ray
from ray_tracer.transformations import Transformation
from ray_tracer.tuples import Tuple

class Intersection():
  # Default constructor
  def __init__(self, t, object):
    self.t = t
    self.object = object

  # Debugging representation
  def __repr__(self):
    return 'Intersection({}, {})'.format(self.t, self.object)
  
  # String representation
  def __str__(self): 
    return '({}, {})'.format(self.t, self.object)
  
  # Method to return the value of the t
  # Used for sorting
  def intersection_value_t(intersection):
    return intersection.t

  # Returns the hit from a list of intersections
  @staticmethod
  def intersections(*intersections):
    result = list(intersections)
    result.sort(key=intersection_value_t)

  # Returns the hit from a list of intersections
  @staticmethod
  def hit(intersections):
    min = None
    for intersection in intersections:
      if (min is None or abs(intersection.t) < min.t):
        min = intersection
    return min