# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

from ray_tracer.colors import Color
from ray_tracer.tuples import Tuple

class Light:
  # Default constructor
  def __init__(self, position, intensity):
    self.position = position
    self.intensity = intensity
  
  # Checks if two light sources are the same
  def __eq__(self, other):
    return self.position == other.position \
      and self.intensity ==  other.intensity

  # Create a light pointing at an specific point
  @staticmethod
  def point_light(position, intensity):
    return Light(position, intensity)
  
  # Debuggin representation
  def __repr__(self):
    return 'Light(({}, {}, {}), ({}, {}, {}))'.format(
      self.position.x, self.position.y, self.position.z,
      self.intensity.r, self.intensity.g, self.intensity.b)
  
  # String representation
  def __str__(self):
    return '(({}, {}, {}), ({}, {}, {}))'.format(
      self.position.x, self.position.y, self.position.z,
      self.intensity.r, self.intensity.g, self.intensity.b)