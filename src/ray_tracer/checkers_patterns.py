# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

import math

from ray_tracer.patterns import Pattern

class Checkers_pattern(Pattern):
    # Default constructor
  def __init__(self, first_color = None, second_color = None):
    super().__init__(first_color, second_color)

  # Debugging representation
  def __repr__(self):
    return 'Checkers_pattern({}, {}, {})'.format(
      self.first_color,self.second_color, self.transform)

  # Returns the color of the checkers pattern at a specific point
  def color_at(self, point):
    calculation = math.floor(point.x) + math.floor(point.y) + math.floor(point.z)
    if calculation % 2 == 0:
      return self.first_color
    return self.second_color