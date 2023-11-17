# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

import math

import ray_tracer.common as common
from ray_tracer.colors import Color
from ray_tracer.matrix import Matrix

from abc import ABC, abstractmethod

class Pattern(ABC):
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
    # Initializes its transformation matrix as the identity matrix
    self.transform = Matrix(4, 4).identity()

  # Debugging representation
  def __repr__(self):
    return 'Pattern({}, {}, {})'.format(
      self.first_color,self.second_color, self.transform)
  
  # String representation
  def __str__(self): 
    return '({}, {}, {})'.format(
      self.first_color,self.second_color, self.transform)
  
  # Returns a bool indicating if two patterns are equal
  def __eq__(self, other):
    self.first_color == other.first_color and \
    self.second_color == other.second_color and \
    self.transform == other.transform

  # Returns the color of the striped pattern at a specific point
  @abstractmethod
  def color_at(self, point):
    pass