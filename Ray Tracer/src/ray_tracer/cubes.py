# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

import math
from ray_tracer.shapes import Shape
from ray_tracer.matrix import Matrix
from ray_tracer.tuples import Tuple
from ray_tracer.intersections import Intersection
import ray_tracer.common as common

class Cube(Shape):
  # Default constructor
  def __init__(self, material=None):
    super().__init__(material)

  # Debugging representation
  def __repr__(self):
    return 'Cube()'

  # Method to get the normal of the sphere at a specific point
  def local_normal_at(self, local_point):
    # Get the component with the highest value
    max_component = max(abs(local_point.x),
                        abs(local_point.y),
                        abs(local_point.z))
    # Return a vector with the value of the highest component
    if max_component == abs(local_point.x):
      return Tuple.vector(local_point.x, 0, 0)
    elif max_component == abs(local_point.y):
      return Tuple.vector(0, local_point.y, 0)
    return Tuple.vector(0, 0, local_point.z)

  def local_intersect(self, local_ray):
    # Get the min and max t values on all the axis of the cube
    x_t_values = Cube.check_axis(local_ray.origin.x, local_ray.direction.x)
    y_t_values = Cube.check_axis(local_ray.origin.y, local_ray.direction.y)
    z_t_values = Cube.check_axis(local_ray.origin.z, local_ray.direction.z)

    # Get the min (first t intersection) as the highest min t value
    t_min = max(x_t_values[0], y_t_values[0], z_t_values[0])
    # Get the max (second t intersection) as the lowest max t value
    t_max = min(x_t_values[1], y_t_values[1], z_t_values[1])

    # If the second intersection is lower than the first
    if t_min > t_max:
      # Return an empty list
      # (There are no intersections)
      return []

    # Return the list of intersections
    return [Intersection(t_min, self), Intersection(t_max, self)]
  
  @staticmethod
  def check_axis(point, direction):
    # Calculate the offset
    t_min_numerator = -1 - point
    t_max_numerator = 1 - point

    # If the direction is positive
    if abs(direction) >= common.EPSILON:
      t_min = t_min_numerator / direction
      t_max = t_max_numerator / direction
    
    # If the direction is negative
    # (To handle divisions by 0)
    else:
      t_min = t_min_numerator * float('inf')
      t_max = t_max_numerator * float('inf')

    # Make sure min is lower than max
    if t_min > t_max:
      # Otherwise swap them
      temp = t_min
      t_min = t_max
      t_max = temp

    # Return a list with the min and the max
    return [t_min, t_max]