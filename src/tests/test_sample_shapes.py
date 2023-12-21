# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

import math
from ray_tracer.tuples import Tuple
from ray_tracer.rays import Ray
from ray_tracer.matrix import Matrix
from ray_tracer.materials import Material
from ray_tracer.transformations import Transformation
from ray_tracer.sample_shapes import Sample_shape

def test_default_transformation():
  s = Sample_shape()
  assert s.transform == Matrix(4, 4).identity()

def test_assign_transformation():
  s = Sample_shape()
  s.set_transform(Transformation.translation(2, 3, 4))
  assert s.transform == Transformation.translation(2, 3, 4)

def test_default_material():
  s = Sample_shape()
  m = s.material
  assert m == Material()

def test_assign_material():
  s = Sample_shape()
  m = Material()
  m.ambient = 1
  s.material = m
  assert s.material == m

def test_assign_material():
  s = Sample_shape()
  m = Material()
  m.ambient = 1
  s.material = m
  assert s.material == m

def test_intersect_scaled_shape():
  r = Ray(Tuple.point(0, 0, -5), Tuple.vector(0, 0, 1))
  s = Sample_shape()
  s.set_transform(Transformation.scaling(2, 2, 2))
  returned_ray = r.intersect(s)
  assert returned_ray.origin == Tuple.point(0, 0, -2.5) and \
         returned_ray.direction == Tuple.vector(0, 0, 0.5)

def test_intersect_translated_shape():
  r = Ray(Tuple.point(0, 0, -5), Tuple.vector(0, 0, 1))
  s = Sample_shape()
  s.set_transform(Transformation.translation(5, 0, 0))
  returned_ray = r.intersect(s)
  assert returned_ray.origin == Tuple.point(-5, 0, -5) and \
         returned_ray.direction == Tuple.vector(0, 0, 1)

def test_normal_translated_shape():
  s = Sample_shape()
  s.set_transform(Transformation.translation(0, 1, 0))
  n = s.normal_at(Tuple.point(0, 1.70711, -0.70711))
  assert n == Tuple.vector(0, 0.70711, -0.70711)

def test_normal_transformed_shape():
  s = Sample_shape()
  m = Transformation.scaling(1, 0.5, 1) * Transformation.rotation_z(math.pi / 5)
  s.set_transform(m)
  n = s.normal_at(Tuple.point(0, math.sqrt(2)/2, -math.sqrt(2)/2))
  assert n == Tuple.vector(0, 0.97014, -0.24254)

