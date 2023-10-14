# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

from ray_tracer.colors import Color

class Material():
  # Default constructor
  def __init__(self):
    self.color = Color(1, 1, 1)
    self.ambient = 0.1
    self.diffuse = 0.9
    self.specular = 0.9
    self.shininess = 200.0

  # Debugging representation
  def __repr__(self):
    return 'Material()'
  
  # String representation
  def __str__(self): 
    return '({}, {}, {}, {}, {})'.format( \
      self.color, self.ambient, self.diffuse, self.specular, self.shininess)
  
  # Checks if two materials are equal
  def __eq__(self, other):
    return self.color == other.color and \
      self.ambient == other.ambient and \
      self.diffuse == other.diffuse and \
      self.specular == other.specular and \
      self.shininess == other.shininess