# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

from ray_tracer.matrix import Matrix
from ray_tracer.materials import Material

from abc import ABC, abstractmethod

class Shape(ABC):
  # Variable to determine the next id
  next_id = 0

  # Default constructor
  def __init__(self, material=None):
    self.transform = Matrix(4, 4).identity()
    self.id = Shape.next_id
    Shape.next_id += 1
    if material is None:
      material = Material()
    self.material = material

  # Debugging representation
  def __repr__(self):
    return 'Shape()'
  
  # String representation
  def __str__(self): 
    return '({}, {})'.format(self.transform, self.id)

  # Returns a bool indicating is two shapes are equal
  def __eq__(self, other):
    return self.id == other.id and \
      self.material == other.material and \
      self.transform == other.transform
  
  # Method to transform the sphere
  def set_transform(self, transform_matrix): 
    self.transform *= transform_matrix

  # Method to transform the pattern of the sphere
  def set_pattern_transform(self, transform_matrix): 
    self.material.pattern.transform *= transform_matrix

  # Metod to get the normal of the shape at an specific point
  def normal_at(self, world_point):
    local_point = self.transform.inverse() * world_point
    local_normal = self.local_normal_at(local_point)
    world_normal = self.transform.inverse().transposing() * local_normal
    world_normal.w = 0
    return world_normal.normalize()

  # Method to get the color on a certain stripe on the shape
  def color_at(self, world_point):
    local_point = self.transform.inverse() * world_point
    pattern_point = self.material.pattern.transform.inverse() * local_point
    return self.material.pattern.color_at(pattern_point)

  # Classes that inherit must implement a method to calculate its normal
  @abstractmethod
  def local_normal_at(self, local_point):
    pass

  # Classes that inherit must implement a method to calcule 
  # their respective intersection
  @abstractmethod
  def local_intersect(self, local_ray):
    pass