# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

from ray_tracer.patterns import Pattern
from ray_tracer.colors import Color

class Sample_pattern(Pattern):
    # Default constructor
  def __init__(self, first_color = None, second_color = None):
    super().__init__(first_color, second_color)

  # Debugging representation
  def __repr__(self):
    return 'Sample_pattern({}, {}, {})'.format(
      self.first_color,self.second_color, self.transform)

  # Returns a color made with the values of the point
  def color_at(self, point):
    return Color(point.x, point.y, point.z)