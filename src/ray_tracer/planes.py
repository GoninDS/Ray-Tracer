# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

import ray_tracer.common as common
from ray_tracer.shapes import Shape
from ray_tracer.tuples import Tuple
from ray_tracer.intersections import Intersection

class Plane(Shape):
    # Default constructor
  def __init__(self, material=None):
    super().__init__(material)

  # Debugging representation
  def __repr__(self):
    return 'Plane()'
  
  # String representation
  def __str__(self): 
    return '({}, {})'.format(self.transform, self.id)
  
  def local_normal_at(self, local_point):
    # Constant value for the normal of a plane
    return Tuple.vector(0, 1, 0)
  
  def local_intersect(self, local_ray):
    if abs(local_ray.direction.y) < common.EPSILON:
      # Return an empty set if there are no intersections
      return None
    # Rest of the logic goes here
    t = -local_ray.origin.y / local_ray.direction.y
    result = []
    result.append(Intersection(t, self))
    return result