# Copyright Luis Javier Campos Duarte
# Modified by Luis David Solano Santamaría & Kenneth Daniel Villalobos Solís

import pytest

from math import sqrt
from tuples import Tuple

def test_tuples_1(): 
  t1 = Tuple.point(4.3, -4.2, 3.1)
  t2 = Tuple.vector(4.3, -4.2, 3.1)
  print(t1)
  print(True == t1.is_point())
  print(True == t2.is_vector())
  assert True == t1.is_point()
  assert True == t2.is_vector()
    
def test_tuples_2(): 
  t1 = Tuple.point(4.3, -4.2, 3.1)
  t2 = Tuple.vector(4.3, -4.2, 3.1)
  assert False == t1.is_vector()
  assert False == t2.is_point()

def test_tuples_add(): 
  t1 = Tuple.point(3, -2, 5)
  t2 = Tuple.vector(-2, 3, 1)
  expected = Tuple.point(1,1,6)
  assert True == ( expected == t1 + t2 )

def test_tuples_subtract(): 
  t1 = Tuple.point(3, 2, 1)
  t2 = Tuple.point(5, 6, 7)
  expected = Tuple.vector(-2, -4, -6)
  assert True == ( expected == (t1 - t2))

def test_tuples_subtract_vector_point():
  t1 = Tuple.point(3, 2, 1)
  t2 = Tuple.vector(5, 6, 7)
  expected = Tuple.point(-2, -4, -6)
  assert True == ( expected == (t1 - t2))
  
def test_tuples_subtract_vectors():
  t1 = Tuple.vector(3, 2, 1)
  t2 = Tuple.vector(5, 6, 7)
  expected = Tuple.vector(-2, -4, -6)
  assert True == ( expected == (t1 - t2))
  
def test_tuples_negating_tuple():
  t1 = Tuple(1, -2, 3, -4)
  expected = Tuple(-1, 2, -3, 4)
  assert True == ( expected == -t1)
  
def test_tuples_multiplying_tuples_scalar():
  t1 = Tuple(1, -2, 3, -4)
  expected = Tuple(3.5, -7, 10.5, -14)
  assert True == ( expected == t1 * 3.5)
  
def test_tuples_multiplying_tuples_scalar_2():
  t1 = Tuple(1, -2, 3, -4)
  expected = Tuple(0.5, -1, 1.5, -2)
  assert True == ( expected == t1 * 0.5)
  
def test_tuples_dividing():
  t1 = Tuple(1, -2, 3, -4)
  expected = Tuple(0.5, -1, 1.5, -2)
  assert True == ( expected == t1 / 2)

def test_tuples_compute_magnitude():
  t1 = Tuple(1,0,0,0)
  assert True == ( t1.equal(t1.magnitude(),1))

def test_tuples_compute_magnitude2():
  t1 = Tuple(0,1,0,0)
  assert True == ( t1.equal(t1.magnitude(),1))   
  
def test_tuples_compute_magnitude3():
  t1 = Tuple(0,0,1,0)
  assert True == ( t1.equal(t1.magnitude(),1))  
  
def test_tuples_compute_magnitude4():
  t1 = Tuple(1,2,3,0)
  assert True == ( t1.equal(t1.magnitude(),sqrt(14)))   
  
def test_tuples_compute_magnitude5():
  t1 = Tuple(-1,-2,-3,0)
  assert True == ( t1.equal(t1.magnitude(),sqrt(14)))   
  
def test_tuples_normalizing_vector():
  t1 = Tuple.vector(4,0,0)
  expected = Tuple.vector(1,0,0)
  assert True == (expected == t1.normalize())
  
def test_tuples_normalizing_vector2():
  t1 = Tuple.vector(1,2,3)
  expected = Tuple.vector(1/sqrt(14),2/sqrt(14),3/sqrt(14))
  assert True == (expected == t1.normalize())  
  
def test_tuples_normalizing_vector3():
  t1 = Tuple.vector(1,2,3)
  normalized = t1.normalize()
  assert True == (normalized.equal(1, normalized.magnitude()))  
  
def test_tuples_dot_product_vectors():
  t1 = Tuple.vector(1,2,3)
  t2 = Tuple.vector(2,3,4)
  assert True == (t1.dot(t2) == 20)
  
def test_tuples_cross_product_vectors():
  t1 = Tuple.vector(1,2,3)
  t2 = Tuple.vector(2,3,4)
  expected1 = Tuple.vector(-1,2,-1)
  expected2 = Tuple.vector(1,-2,1)
  assert True == (t1.cross(t2) == expected1)
  assert True == (t2.cross(t1) == expected2)
  
def test_tuples_reflecting_vector_45():
  t1 = Tuple.vector(1, -1, 0)
  t2 = Tuple.vector(0, 1, 0)
  expected = Tuple.vector(1, 1, 0)
  assert True == (t1.reflect(t2) == expected) 

def test_tuples_reflecting_vector_slanted_surface():
  t1 = Tuple.vector(0, -1, 0)
  t2 = Tuple.vector(sqrt(2)/2, sqrt(2)/2, 0)
  expected = Tuple.vector(1, 0, 0)
  assert True == (t1.reflect(t2) == expected) 