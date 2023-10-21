# Copyright Luis Javier Campos Duarte
# Modified by Luis David Solano Santamaría & Kenneth Daniel Villalobos Solís

import math
import pytest
from ray_tracer.matrix import Matrix
from ray_tracer.transformations import Transformation  # Asumiendo que tienes una clase llamada 'Transformations' en un archivo llamado 'transformations.py'
from ray_tracer.tuples import Tuple  # Asumiendo que tienes una clase llamada 'Tuple' para representar tuplas

def test_multiplying_translation():
  p = Tuple.point(-3, 4, 5)
  expected = Tuple.point(2, 1, 7)
  t = Transformation.translation(5, -3, 2)
  result = t * p
  assert result == expected

def test_multiplying_translation_inverse():
  p = Tuple.point(-3, 4, 5)
  expected = Tuple.point(-8, 7, 3)
  a = Transformation.translation(5, -3, 2)
  inverse = a.inverse()
  result = inverse * p
  assert result == expected

def test_multiplying_translation_vector():
  p = Tuple.vector(-3, 4, 5)
  a = Transformation.translation(5, -3, 2)
  result = a * p
  assert result == p

def test_scaling_matrix_point():
  p = Tuple.point(-4, 6, 8)
  expected = Tuple.point(-8, 18, 32)
  transform = Transformation.scaling(2, 3, 4)
  result = transform * p
  assert result == expected

def test_scaling_matrix_vector():
  v = Tuple.vector(-4, 6, 8)
  expected = Tuple.vector(-8, 18, 32)
  transform = Transformation.scaling(2, 3, 4)
  result = transform * v
  assert result == expected

def test_scaling_inverse_vector():
  v = Tuple.vector(-4, 6, 8)
  expected = Tuple.vector(-2, 2, 2)
  transform = Transformation.scaling(2, 3, 4)
  inverse = transform.inverse()
  result = inverse * v
  assert result == expected

def test_reflection_scaling():
  p = Tuple.point(2, 3, 4)
  expected = Tuple.point(-2, 3, 4)
  transform = Transformation.scaling(-1, 1, 1)
  result = transform * p
  assert result == expected

def test_rotating_point_x():
  p = Tuple.point(0, 1, 0)
  expected1 = Tuple.point(0, math.sqrt(2) / 2, math.sqrt(2) / 2)
  expected2 = Tuple.point(0, 0, 1)
  halfQuarter = Transformation.rotation_x(math.pi / 4)
  fullQuarter = Transformation.rotation_x(math.pi / 2)
  result1 = halfQuarter * p
  result2 = fullQuarter * p
  assert result1 == expected1
  assert result2 == expected2

def test_rotating_inverse_point_x():
  p = Tuple.point(0, 1, 0)
  expected1 = Tuple.point(0, math.sqrt(2) / 2, -math.sqrt(2) / 2)
  halfQuarter = Transformation.rotation_x(math.pi / 4)
  inv = halfQuarter.inverse()
  result = inv * p
  assert result == expected1

def test_rotating_point_y():
  p = Tuple.point(0, 0, 1)
  expected1 = Tuple.point(math.sqrt(2) / 2, 0, math.sqrt(2) / 2)
  expected2 = Tuple.point(1, 0, 0)
  halfQuarter = Transformation.rotation_y(math.pi / 4)
  fullQuarter = Transformation.rotation_y(math.pi / 2)
  result1 = halfQuarter * p
  result2 = fullQuarter * p
  assert result1 == expected1
  assert result2 == expected2

def test_rotating_point_z():
  p = Tuple.point(0, 1, 0)
  expected1 = Tuple.point(-math.sqrt(2) / 2, math.sqrt(2) / 2, 0)
  expected2 = Tuple.point(-1, 0, 0)
  halfQuarter = Transformation.rotation_z(math.pi / 4)
  fullQuarter = Transformation.rotation_z(math.pi / 2)
  result1 = halfQuarter * p
  result2 = fullQuarter * p
  assert result1 == expected1
  assert result2 == expected2

def test_shearing_x_in_y():
  p = Tuple.point(2, 3, 4)
  expected = Tuple.point(5, 3, 4)
  transform = Transformation.shearing(1, 0, 0, 0, 0, 0)
  result = transform * p
  assert result == expected

def test_shearing_x_in_z():
  p = Tuple.point(2, 3, 4)
  expected = Tuple.point(6, 3, 4)
  transform = Transformation.shearing(0, 1, 0, 0, 0, 0)
  result = transform * p
  assert result == expected

def test_shearing_y_in_x():
  p = Tuple.point(2, 3, 4)
  expected = Tuple.point(2, 5, 4)
  transform = Transformation.shearing(0, 0, 1, 0, 0, 0)
  result = transform * p
  assert result == expected

def test_shearing_y_in_z():
  p = Tuple.point(2, 3, 4)
  expected = Tuple.point(2, 7, 4)
  transform = Transformation.shearing(0, 0, 0, 1, 0, 0)
  result = transform * p
  assert result == expected

def test_shearing_z_in_x():
  p = Tuple.point(2, 3, 4)
  expected = Tuple.point(2, 3, 6)
  transform = Transformation.shearing(0, 0, 0, 0, 1, 0)
  result = transform * p
  assert result == expected

def test_shearing_z_in_y():
  p = Tuple.point(2, 3, 4)
  expected = Tuple.point(2, 3, 7)
  transform = Transformation.shearing(0, 0, 0, 0, 0, 1)
  result = transform * p
  assert result == expected

def test_individual_transformations():
  p = Tuple.point(1, 0, 1)
  expected1 = Tuple.point(1, -1, 0)
  expected2 = Tuple.point(5, -5, 0)
  expected3 = Tuple.point(15, 0, 7)
  A = Transformation.rotation_x(math.pi / 2)
  B = Transformation.scaling(5, 5, 5)
  C = Transformation.translation(10, 5, 7)
  p2 = A * p
  assert p2 == expected1
  p3 = B * p2
  assert p3 == expected2
  p4 = C * p3
  assert p4 == expected3

def test_chained_transformations():
  p = Tuple.point(1, 0, 1)
  expected1 = Tuple.point(15, 0, 7)
  A = Transformation.rotation_x(math.pi / 2)
  B = Transformation.scaling(5, 5, 5)
  C = Transformation.translation(10, 5, 7)
  T = C * B * A
  result = T * p
  assert result == expected1

def test_transformation_matrix_default_orientation():
  p_from = Tuple.point(0,0,0)
  p_to = Tuple.point(0,0,-1)
  p_up = Tuple.vector(0,1,0)
  transformation_matrix = Transformation.view_transform(p_from, p_to, p_up)
  assert transformation_matrix == transformation_matrix.identity()

def test_view_transformation_positive_z():
  p_from = Tuple.point(0,0,0)
  p_to = Tuple.point(0,0,1)
  p_up = Tuple.vector(0,1,0)
  transformation_matrix = Transformation.view_transform(p_from, p_to, p_up)
  assert transformation_matrix == Transformation.scaling(-1, 1, -1)
  
def test_view_transformation_moves_world():
  p_from = Tuple.point(0,0,8)
  p_to = Tuple.point(0,0,0)
  p_up = Tuple.vector(0,1,0)
  transformation_matrix = Transformation.view_transform(p_from, p_to, p_up)
  assert transformation_matrix == Transformation.translation(0, 0, -8)

def test_arbitrary_view_transformation():
  p_from = Tuple.point(1, 3, 2)
  p_to = Tuple.point(4, -2, 8)
  p_up = Tuple.vector(1, 1, 0)
  transformation_matrix = Transformation.view_transform(p_from, p_to, p_up)
  
  expected = Matrix(4, 4)
  
  expected[0][0] = -0.50709
  expected[0][1] = 0.50709
  expected[0][2] = 0.67612
  expected[0][3] = -2.36643
  
  expected[1][0] = 0.76772
  expected[1][1] = 0.60609
  expected[1][2] = 0.12122
  expected[1][3] = -2.82843
  
  expected[2][0] = -0.35857
  expected[2][1] = 0.59761
  expected[2][2] = -0.71714
  expected[2][3] = 0.00000
  
  expected[3][0] = 0.00000
  expected[3][1] = 0.00000
  expected[3][2] = 0.00000
  expected[3][3] = 1.00000
  
  assert transformation_matrix == expected