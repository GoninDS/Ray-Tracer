# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

import math

from ray_tracer.patterns import Pattern

class Gradient_pattern(Pattern):
    # Default constructor
  def __init__(self, first_color = None, second_color = None):
    super().__init__(first_color, second_color)

  # Debugging representation
  def __repr__(self):
    return 'Gradient_pattern({}, {}, {})'.format(
      self.first_color,self.second_color, self.transform)

  # Returns the color of the gradient pattern at a specific point
  def color_at(self, point):
    distance = self.second_color - self.first_color
    fraction = point.x - math.floor(point.x)
    return self.first_color + distance * fraction