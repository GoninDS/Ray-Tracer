# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

import math

import ray_tracer.common as common
from ray_tracer.colors import Color

class Pattern():
    # Default constructor
  def __init__(self, first_color = None, second_color = None):
    # First is none, assign a default color
    if first_color is None:
      self.first_color = Color.white()
    else:
      self.first_color = first_color
    # Second is none, assign a default color
    if second_color is None:
      self.second_color = Color.black()
    else:
      self.second_color = second_color

  # Debugging representation
  def __repr__(self):
    return 'Pattern({}, {})'.format(self.first_color, self.second_color)
  
  # String representation
  def __str__(self): 
    return '({}, {})'.format(self.first_color, self.second_color)
  
  # Returns a striped pattern of two colors
  @staticmethod
  def striped_pattern(first_color, second_color):
    return Pattern(first_color, second_color)

  # Returns the color of the striped pattern at a specific point
  def stripe_at(self, point):
    # If it is divisible by 0 return the first color
    if math.floor(point.x) % 2 == 0:
      return self.first_color
    # If not, return the second color
    return self.second_color