# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

import math

from ray_tracer.patterns import Pattern

class Striped_pattern(Pattern):
    # Default constructor
  def __init__(self, first_color = None, second_color = None):
    super().__init__(first_color, second_color)

  # Debugging representation
  def __repr__(self):
    return 'Striped_pattern({}, {}, {})'.format(
      self.first_color,self.second_color, self.transform)

  # Returns the color of the striped pattern at a specific point
  def color_at(self, point):
    # If it is divisible by 0 return the first color
    if math.floor(point.x) % 2 == 0:
      return self.first_color
    # If not, return the second color
    return self.second_color