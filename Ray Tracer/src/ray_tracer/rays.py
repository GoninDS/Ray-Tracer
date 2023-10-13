# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

from tuples import Tuple
from transformations import Transformation

class Ray:
  # Default constructor
  def __init__(self, origin, direction):
    self.origin = origin
    self.direction = direction

  # Debugging representation
  def __repr__(self):
    return 'Ray(({}, {}, {}), ({}, {}, {}))'.format(
      self.origin.x, self.origin.y, self.origin.z,
      self.direction.x, self.direction.y, self.direction.z)
  
  # String representation
  def __str__(self): 
    return '(({}, {}, {}), ({}, {}, {}))'.format(
      self.origin.x, self.origin.y, self.origin.z,
      self.direction.x, self.direction.y, self.direction.z)

  # Calculate the position of the ray on a given t
  def position(self, t):
    return (self.direction * t) + self.origin
  
  # Returns the transformed version of the ray
  def transform(self, transformation):
    new_ray = Ray(Tuple.point(0, 0, 0), Tuple.vector(0, 0, 0))
    new_ray.origin = transformation * self.origin
    new_ray.direction = transformation * self.direction
    return new_ray