# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

import math
from ray_tracer.shapes import Shape
from ray_tracer.tuples import Tuple
from ray_tracer.intersections import Intersection
import ray_tracer.common as common

class Cone(Shape):
  # Default constructor
  def __init__(self, material=None):
    super().__init__(material)
    self.minimum = float('-inf')
    self.maximum = float('inf')
    self.closed = False

  # Debugging representation
  def __repr__(self):
    return 'Cone()'
  
  # String representation
  def __str__(self): 
    return '({}, {}, {}, {}, {})'.format(self.transform, self.id,
                                         self.material, self.minimum,
                                         self.maximum)

  # Method to get the normal of the cone at a specific point
  def local_normal_at(self, local_point):
    # compute the square of the distance from the y axis
    distance = local_point.x**2 + local_point.z**2

    if distance < 1 and local_point.y >= self.maximum - common.EPSILON:
      return Tuple.vector(0, 1, 0)
    elif distance < 1 and local_point.y <= self.minimum + common.EPSILON:
      return Tuple.vector(0, -1, 0)

    y = math.sqrt(local_point.x**2 + local_point.z**2)
    if local_point.y > 0:
      y = -y
    return Tuple.vector(local_point.x, y, local_point.z)

  # Method to intersect a cone with a ray
  def local_intersect(self, local_ray):
    intersections = []
    # Calculate a
    a = local_ray.direction.x**2 - local_ray.direction.y**2 + \
        local_ray.direction.z**2
    # Calculate b
    b = 2 * local_ray.origin.x * local_ray.direction.x - \
        2 * local_ray.origin.y * local_ray.direction.y + \
        2 * local_ray.origin.z * local_ray.direction.z
    # Calculate c
    c = local_ray.origin.x**2 - local_ray.origin.y**2 + local_ray.origin.z**2

    # If a and b are 0, the ray misses
    if (a != 0 or b != 0):
      # If a is 0 but b isn´t
      if (a == 0):
        t = -c / (2 * b)
        intersections.append(Intersection(t, self))

      # If a is non zero is the same as cylinders
      else:
        # Calculate the discriminant
        discriminant = b**2 - 4 * a * c

        # ray does not intersect the cone
        if discriminant >= 0:
          # Get the intersections t´s
          t_0 = (-b - math.sqrt(discriminant)) / (2 * a)
          t_1 = (-b + math.sqrt(discriminant)) / (2 * a)

          # If the t´s are in opposite order, swap them
          if t_0 > t_1:
            temp = t_0
            t_0 = t_1
            t_1 = temp

          # Add the intersections if the are within the dimensions
          # of the cone
          y_0 = local_ray.origin.y + t_0 * local_ray.direction.y
          if self.minimum < y_0 and y_0 < self.maximum:
            intersections.append(Intersection(t_0, self))

          y_1 = local_ray.origin.y + t_1 * local_ray.direction.y
          if self.minimum < y_1 and y_1 < self.maximum:
            intersections.append(Intersection(t_1, self))
    
    # Check intersections with the cap
    self.intersect_caps(local_ray, intersections)

    # Return the intersections
    return intersections
  
  # Function to check if the intersection at the t is within
  # a radius of 1 (radius of the cone) from the y axis
  @staticmethod
  def check_cap(ray, t, y):
    x = ray.origin.x + t * ray.direction.x
    z = ray.origin.z + t * ray.direction.z

    if (x**2 + z**2) <= abs(y):
      return True
    return False
  
  def intersect_caps(self, ray, intersections):
    # caps only matter if the cylinder is closed, and might possibly be
    # intersected by the ray.
    if abs(ray.direction.y) <= common.EPSILON or not self.closed:
      return
    
    # check for an intersection with the lower end cap by intersecting
    # the ray with the plane at y = minimum
    t = (self.minimum - ray.origin.y) / ray.direction.y
    if Cone.check_cap(ray, t, self.minimum):
      intersections.append(Intersection(t, self))

    # check for an intersection with the upper end cap by intersecting
    # the ray with the plane at y = maximum
    t = (self.maximum - ray.origin.y) / ray.direction.y
    if Cone.check_cap(ray, t, self.maximum):
      intersections.append(Intersection(t, self))