# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

import math

from ray_tracer.tuples import Tuple
from ray_tracer.intersection import Intersection

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
  
  # Returns the intersection bew
  def intersect(self, object):
    # Get the transformed ray
    transformed_ray = self.transform(object.transform.inverse())
    # Create a list of intersections
    results =  []

    # Calculate a, b and c
    sphere_to_ray = transformed_ray.origin - Tuple.point(0, 0, 0)
    a = transformed_ray.direction.dot(transformed_ray.direction)
    b = 2 * transformed_ray.direction.dot(sphere_to_ray)
    c = sphere_to_ray.dot(sphere_to_ray) - 1

    # Calculate the discriminant
    discriminant = (b ** 2) - (4 * a * c)
    # If there are positive intersections
    if discriminant >= 0:
      # Add the first intersection
      t1 = (-b - math.sqrt(discriminant)) / (2 * a)
      results.append(Intersection(t1, object))

      # If there were 2 intersections
      if discriminant > 0:
        # Add the second intersection
        t2 = (-b + math.sqrt(discriminant)) / (2 * a)
        results.append(Intersection(t2, object))

    # Return the list of intersections
    return results