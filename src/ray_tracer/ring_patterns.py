# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

import math

from ray_tracer.patterns import Pattern

class Ring_pattern(Pattern):
    # Default constructor
  def __init__(self, first_color = None, second_color = None):
    super().__init__(first_color, second_color)

  # Debugging representation
  def __repr__(self):
    return 'Ring_pattern({}, {}, {})'.format(
      self.first_color, self.second_color, self.transform)

  # Returns the color of the ring pattern at a specific point
  def color_at(self, point):
    # Return the first color if it is event
    calculate = math.floor(math.sqrt(point.x ** 2 + point.z ** 2))
    if calculate % 2 == 0:
      return self.first_color
    # Return the second color if not
    return self.second_color