# Copyright Luis Javier Campos Duarte
# Modified by Luis David Solano Santamaría & Kenneth Daniel Villalobos Solís

import math

from ray_tracer.spheres import Sphere
from ray_tracer.planes import Plane
from ray_tracer.intersections import Intersection
from ray_tracer.computations import Computation
from ray_tracer.transformations import Transformation
from ray_tracer.tuples import Tuple
from ray_tracer.rays import Ray
import ray_tracer.common as common

def test_intersection_encapsulates_t():
  s1 = Sphere()
  inter = Intersection(3.5, s1)
  assert inter.shape.id == s1.id
  assert inter.t == 3.5

def test_aggregating_intersections():
  s = Sphere()
  i1 = Intersection(1, s)
  i2 = Intersection(2, s)
  xs = Intersection.intersections(i1, i2)
  print(str(xs))
  assert len(xs) == 2
  assert xs[0].t == 1
  assert xs[1].t == 2

def test_hit_positive_t():
  s = Sphere()
  i1 = Intersection(1, s)
  i2 = Intersection(2, s)
  xs = Intersection.intersections(i1, i2)
  result = i1.hit(xs)
  assert result == i1

def test_hit_positive_negative_t():
  s = Sphere()
  i1 = Intersection(-1.0, s)
  i2 = Intersection(1, s)
  xs = Intersection.intersections(i1, i2)
  result = i1.hit(xs)
  assert result == i2

def test_hit_negative_t():
  s = Sphere()
  i1 = Intersection(-2, s)
  i2 = Intersection(-1, s)
  xs = Intersection.intersections(i1, i2)
  result = i1.hit(xs)
  assert result is None

def test_lowest_nonnegative():
  s = Sphere()
  i1 = Intersection(5, s)
  i2 = Intersection(7, s)
  i3 = Intersection(-3, s)
  i4 = Intersection(2, s)
  xs = Intersection.intersections(i1, i2, i3, i4)
  result = i1.hit(xs)
  assert result == i4

def test_precomputing_state():
  shape = Sphere()
  origin = Tuple.point(0, 0, -5)
  direction = Tuple.vector(0, 0, 1)
  r = Ray(origin, direction)
  i = Intersection(4, shape)
  comps = Computation.prepare_computations(i, r)
  pointR = Tuple.point(0, 0, -1)
  vectorR = Tuple.vector(0, 0, -1)
  assert comps.t == i.t
  assert comps.shape == i.shape
  assert comps.point == pointR
  assert comps.eyev == vectorR
  assert comps.normalv == vectorR

def test_hit_intersection_outside():
  shape = Sphere()
  origin = Tuple.point(0, 0, -5)
  direction = Tuple.vector(0, 0, 1)
  r = Ray(origin, direction)
  i = Intersection(4, shape)
  comps = Computation.prepare_computations(i, r)
  assert not comps.inside

def test_hit_intersection_inside():
  shape = Sphere()
  origin = Tuple.point(0, 0, 0)
  direction = Tuple.vector(0, 0, 1)
  r = Ray(origin, direction)
  i = Intersection(1, shape)
  comps = Computation.prepare_computations(i, r)
  pointR = Tuple.point(0, 0, 1)
  vectorR = Tuple.vector(0, 0, -1)
  assert comps.inside
  assert comps.point == pointR
  assert comps.eyev == vectorR
  assert comps.normalv == vectorR

def test_hit_should_offset_point():
  r = Ray(Tuple.point(0, 0, -5), Tuple.vector(0, 0, 1))
  shape = Sphere()
  shape.transform = Transformation.translation(0, 0, 1)
  i = Intersection(5, shape)
  comps = Computation.prepare_computations(i, r)
  assert comps.over_point.z < -common.EPSILON/2
  assert comps.point.z > comps.over_point.z

def test_precomputing_reflect_vector():
  plane = Plane()
  ray = Ray(Tuple.point(0, 1, -1),
          Tuple.vector(0, -math.sqrt(2)/2, math.sqrt(2)/2))
  intersection = Intersection(math.sqrt(2), plane)
  comps = Computation.prepare_computations(intersection, ray)
  assert comps.reflectv == Tuple.vector(0, math.sqrt(2)/2, math.sqrt(2)/2)