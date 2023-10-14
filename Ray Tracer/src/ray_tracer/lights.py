# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

from ray_tracer.colors import Color
from ray_tracer.tuples import Tuple

class Light:
  # Default constructor
  def __init__(self, position, intensity):
    self.position = position
    self.intensity = intensity
  
  # Create a light pointing at an specific point
  @staticmethod
  def point_light(position, intensity):
    return Light(position, intensity)