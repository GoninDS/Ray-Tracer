# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

from ray_tracer.matrix import Matrix
from ray_tracer.tuples import Tuple
from ray_tracer.materials import Material

class Sphere():
  # Variable to determine the next id
  next_id = 0

  # Default constructor
  def __init__(self, material=None):
    self.transform = Matrix(4, 4).identity()
    self.id = Sphere.next_id
    Sphere.next_id += 1
    if material is None:
      material = Material()
    self.material = material

  # Debugging representation
  def __repr__(self):
    return 'Sphere()'
  
  # String representation
  def __str__(self): 
    return '({}, {})'.format(self.transform, self.id)

  # Returns a bool indicating is two spheres are equal
  def __eq__(self, other):
    return self.id == other.id and \
    self.material == other.material and \
    self.transform == other.transform
  
  # Method to transform the sphere
  def set_transform(self, transform_matrix): 
    self.transform *= transform_matrix

  # Method to get the normal of the sphere at a specific point
  def normal_at(self, world_point):
    sphere_point = self.transform.inverse() * world_point
    sphere_normal = sphere_point - Tuple.point(0, 0, 0)
    world_normal = self.transform.inverse().transposing() * sphere_normal
    world_normal.w = 0
    return world_normal.normalize()