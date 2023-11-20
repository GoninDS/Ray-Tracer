# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

from ray_tracer.colors import Color

class Material():
  # Default constructor
  def __init__(self, color = Color(1, 1, 1), ambient = 0.1,
    diffuse = 0.9, specular = 0.9, shininess = 200.0, reflectiveness = 0.0,
    pattern = None):
    self.color = color
    self.ambient = ambient
    self.diffuse = diffuse
    self.specular = specular
    self.shininess = shininess
    self.reflectiveness = reflectiveness
    self.pattern = pattern

  # Debugging representation
  def __repr__(self):
    return 'Material()'
  
  # String representation
  def __str__(self): 
    return '({}, {}, {}, {}, {}, {}, {})'.format( \
      self.color, self.ambient, self.diffuse, self.specular, self.shininess,
      self.reflectiveness, self.pattern)
  
  # Checks if two materials are equal
  def __eq__(self, other):
    return self.color == other.color and \
      self.ambient == other.ambient and \
      self.diffuse == other.diffuse and \
      self.specular == other.specular and \
      self.shininess == other.shininess and \
      self.reflectiveness == other.reflectiveness and \
      self.pattern == other.pattern