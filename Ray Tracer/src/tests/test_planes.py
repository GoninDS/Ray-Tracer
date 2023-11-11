# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

import pytest

from ray_tracer.tuples import Tuple
from ray_tracer.rays import Ray
from ray_tracer.planes import Plane

def test_plane_normal():
  p = Plane()
  n1 = p.local_normal_at(Tuple.point(0, 0, 0))
  n2 = p.local_normal_at(Tuple.point(10, 0, -10))
  n3 = p.local_normal_at(Tuple.point(-5, 0, 150))
  assert n1 == Tuple.vector(0, 1, 0) and \
         n2 == Tuple.vector(0, 1, 0) and \
         n3 == Tuple.vector(0, 1, 0)

def test_plane_parallel_intersection():
  p = Plane()
  r = Ray(Tuple.point(0, 10, 0), Tuple.vector(0, 0, 1))
  xs = p.local_intersect(r)
  assert xs is None

def test_plane_coplanar_intersection():
  p = Plane()
  r = Ray(Tuple.point(0, 0, 0), Tuple.vector(0, 0, 1))
  xs = p.local_intersect(r)
  assert xs is None
 
def test_plane_above_intersection():
  p = Plane()
  r = Ray(Tuple.point(0, 1, 0), Tuple.vector(0, -1, 0))
  xs = p.local_intersect(r)
  assert len(xs) == 1 and \
         xs[0].t == 1 and \
         xs[0].shape == p

def test_plane_below_intersection():
  p = Plane()
  r = Ray(Tuple.point(0, -1, 0), Tuple.vector(0, 1, 0))
  xs = p.local_intersect(r)
  assert len(xs) == 1 and \
         xs[0].t == 1 and \
         xs[0].shape == p
  