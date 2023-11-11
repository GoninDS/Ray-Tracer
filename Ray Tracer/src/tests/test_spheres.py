# Copyright Luis Javier Campos Duarte
# Modified by Luis David Solano Santamaría & Kenneth Daniel Villalobos Solís

import pytest
from ray_tracer.rays import Ray
from ray_tracer.spheres import Sphere
from ray_tracer.intersections import Intersection
from ray_tracer.transformations import Transformation
from ray_tracer.tuples import Tuple
from ray_tracer.materials import Material
from ray_tracer.matrix import Matrix

def test_two_points_intersection_sphere():
  origin = Tuple.point(0, 0, -5)
  direction = Tuple.vector(0, 0, 1)
  ray = Ray(origin, direction)
  sphere = Sphere()
  intersections = ray.intersect(sphere)
  print(str(intersections[0].t))
  print(str(intersections[1].t))
  assert len(intersections) == 2
  assert intersections[0].t == 4.0
  assert intersections[1].t == 6.0

def test_one_point_tangent_sphere():
  origin = Tuple.point(0, 1, -5)
  direction = Tuple.vector(0, 0, 1)
  ray = Ray(origin, direction)
  sphere = Sphere()
  intersections = ray.intersect(sphere)
  assert len(intersections) == 1
  assert intersections[0].t == 5.0

def test_ray_misses_sphere():
  origin = Tuple.point(0, 2, -5)
  direction = Tuple.vector(0, 0, 1)
  ray = Ray(origin, direction)
  sphere = Sphere()
  intersections = ray.intersect(sphere)
  assert len(intersections) == 0

def test_ray_originates_inside_sphere():
  origin = Tuple.point(0, 0, 0)
  direction = Tuple.vector(0, 0, 1)
  ray = Ray(origin, direction)
  sphere = Sphere()
  intersections = ray.intersect(sphere)
  assert len(intersections) == 2
  assert intersections[0].t == -1.0
  assert intersections[1].t == 1.0

def test_sphere_behind_ray():
  origin = Tuple.point(0, 0, 5)
  direction = Tuple.vector(0, 0, 1)
  ray = Ray(origin, direction)
  sphere = Sphere()
  intersections = ray.intersect(sphere)
  assert len(intersections) == 2
  assert intersections[0].t == -6.0
  assert intersections[1].t == -4.0

def test_object_on_intersection():
  origin = Tuple.point(0, 0, -5)
  direction = Tuple.vector(0, 0, 1)
  ray = Ray(origin, direction)
  sphere = Sphere()
  intersections = ray.intersect(sphere)
  assert len(intersections) == 2
  assert intersections[0].shape.id == sphere.id
  assert intersections[1].shape.id == sphere.id

def test_default_transformation():
  sphere = Sphere()
  compare = sphere.transform
  ident = Matrix(4,4).identity()
  expected = ident
  assert compare == expected

def test_changing_transformation():
  sphere = Sphere()
  translation = Transformation.translation(2, 3, 4)
  sphere.set_transform(translation)
  expected = translation
  assert sphere.transform == expected

def test_intersecting_scaled_sphere():
  origin = Tuple.point(0, 0, -5)
  direction = Tuple.vector(0, 0, 1)
  ray = Ray(origin, direction)
  scaling = Transformation.scaling(2, 2, 2)
  sphere = Sphere()
  sphere.set_transform(scaling)
  intersections = ray.intersect(sphere)
  assert len(intersections) == 2
  assert intersections[0].t == 3
  assert intersections[1].t == 7

def test_intersecting_translated_sphere():
  origin = Tuple.point(0, 0, -5)
  direction = Tuple.vector(0, 0, 1)
  ray = Ray(origin, direction)
  translation = Transformation.translation(5, 0, 0)
  sphere = Sphere()
  sphere.set_transform(translation)
  intersections = ray.intersect(sphere)
  assert len(intersections) == 0

def test_normal_sphere_x_axis():
  sphere = Sphere()
  Point = Tuple.point(1, 0, 0)
  expected = Tuple.vector(1, 0, 0)
  normal = sphere.normal_at(Point)
  assert normal == expected

def test_normal_sphere_y_axis():
  sphere = Sphere()
  Point = Tuple.point(0, 1, 0)
  expected = Tuple.vector(0, 1, 0)
  normal = sphere.normal_at(Point)
  assert normal == expected

def test_normal_sphere_z_axis():
  sphere = Sphere()
  Point = Tuple.point(0, 0, 1)
  expected = Tuple.vector(0, 0, 1)
  normal = sphere.normal_at(Point)
  assert normal == expected

def test_normal_sphere_non_axial():
  sphere = Sphere()
  Point = Tuple.point((3 ** 0.5) / 3, (3 ** 0.5) / 3, (3 ** 0.5) / 3)
  expected = Tuple.vector((3 ** 0.5) / 3, (3 ** 0.5) / 3, (3 ** 0.5) / 3)
  normal = sphere.normal_at(Point)
  assert normal == expected

def test_normal_normalized_vector():
  sphere = Sphere()
  Point = Tuple.point((3 ** 0.5) / 3, (3 ** 0.5) / 3, (3 ** 0.5) / 3)
  normal = sphere.normal_at(Point)
  assert normal == normal.normalize()

def test_normal_translated_sphere():
  sphere = Sphere()
  sphere.set_transform(Transformation.translation(0, 1, 0))
  Point = Tuple.point(0, 1.70711, -0.70711)
  expected = Tuple.vector(0, 0.70711, -0.70711)
  normal = sphere.normal_at(Point)
  assert normal == expected

def test_normal_transformed_sphere():
  sphere = Sphere()
  m = Transformation.scaling(1, 0.5, 1) * Transformation.rotation_z(3.14159/5)
  sphere.set_transform(m)
  Point = Tuple.point(0, (2 ** 0.5) / 2, -(2 ** 0.5) / 2)
  expected = Tuple.vector(0, 0.97014, -0.24254)
  normal = sphere.normal_at(Point)
  assert normal == expected

def test_sphere_default_material():
  sphere = Sphere()
  m = sphere.material
  expected = Material()
  assert m == expected

def test_sphere_assigned_material():
  sphere = Sphere()
  m = Material()
  m.ambient = 1
  sphere.material = m
  assert m == sphere.material
