# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

import math
from ray_tracer.shapes import Shape
from ray_tracer.matrix import Matrix
from ray_tracer.tuples import Tuple
from ray_tracer.intersections import Intersection

class Sphere(Shape):
  # Default constructor
  def __init__(self, material=None):
    super().__init__(material)

  # Creates a glass sphere
  @staticmethod
  def glass_sphere():
    sphere = Sphere()
    sphere.transform = Matrix(4, 4).identity()
    sphere.material.transparency = 1.0
    sphere.material.refractive_index = 1.5
    return sphere

  # Debugging representation
  def __repr__(self):
    return 'Sphere()'
  
  # Method to get the normal of the sphere at a specific point
  def local_normal_at(self, local_point):
    return local_point - Tuple.point(0, 0, 0)

  def local_intersect(self, local_ray):
    # Create a list of intersections
    results =  []
    # Calculate a, b and c
    sphere_to_ray = local_ray.origin - Tuple.point(0, 0, 0)
    a = local_ray.direction.dot(local_ray.direction)
    b = 2 * local_ray.direction.dot(sphere_to_ray)
    c = sphere_to_ray.dot(sphere_to_ray) - 1
    # Calculate the discriminant
    discriminant = (b ** 2) - (4 * a * c)
    # If there are positive intersections
    if discriminant >= 0:
      # Add the first intersection
      t1 = (-b - math.sqrt(discriminant)) / (2 * a)
      results.append(Intersection(t1, self))
      # If there were 2 intersections
      if discriminant > 0:
        # Add the second intersection
        t2 = (-b + math.sqrt(discriminant)) / (2 * a)
        results.append(Intersection(t2, self))
    # Return the list of intersections
    return results