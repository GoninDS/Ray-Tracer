# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

import math
from ray_tracer.cones import Cone
from ray_tracer.rays import Ray
from ray_tracer.tuples import Tuple
import ray_tracer.common as common

def test_ray_intersects_cone():
  cone = Cone()
  ray_1 = Ray(Tuple.point(0, 0, -5), Tuple.vector(0, 0, 1).normalize())
  ray_2 = Ray(Tuple.point(0, 0, -5), Tuple.vector(1, 1, 1).normalize())
  ray_3 = Ray(Tuple.point(1, 1, -5), Tuple.vector(-0.5, -1, 1).normalize())

  xs_1 = cone.local_intersect(ray_1)
  xs_2 = cone.local_intersect(ray_2)
  xs_3 = cone.local_intersect(ray_3)

  assert len(xs_1) == 2 and \
            xs_1[0].t == 5 and xs_1[1].t == 5 and \
         len(xs_2) == 2 and \
            common.equal(xs_2[0].t, 8.66025) and \
            common.equal(xs_2[1].t, 8.66025) and \
         len(xs_3) == 2 and \
            common.equal(xs_3[0].t, 4.55006) and \
            common.equal(xs_3[1].t, 49.44994)

def test_parallel_ray_intersects_half_cone():
  cone = Cone()
  ray = Ray(Tuple.point(0, 0, -1), Tuple.vector(0, 1, 1).normalize())
  xs = cone.local_intersect(ray)

  assert len(xs) == 1 and \
            common.equal(xs[0].t, 0.35355)

def test_intersect_cones_end_caps():
  cone = Cone()
  cone.minimum = -0.5
  cone.maximum = 0.5
  cone.closed = True

  ray_1 = Ray(Tuple.point(0, 0, -5), Tuple.vector(0, 1, 0).normalize())
  ray_2 = Ray(Tuple.point(0, 0, -0.25), Tuple.vector(0, 1, 1).normalize())
  ray_3 = Ray(Tuple.point(0, 0, -0.25), Tuple.vector(0, 1, 0).normalize())

  xs_1 = cone.local_intersect(ray_1)
  xs_2 = cone.local_intersect(ray_2)
  xs_3 = cone.local_intersect(ray_3)

  assert len(xs_1) == 0 and \
         len(xs_2) == 2 and \
         len(xs_3) == 4

def test_normal_on_cone():
  cone = Cone()
  point_1 = Tuple.point(0, 0, 0)
  point_2 = Tuple.point(1, 1, 1)
  point_3 = Tuple.point(-1, -1, 0)

  normal_1 = cone.local_normal_at(point_1)
  normal_2 = cone.local_normal_at(point_2)
  normal_3 = cone.local_normal_at(point_3)

  assert normal_1 == Tuple.vector(0, 0, 0) and \
         normal_2 == Tuple.vector(1, -math.sqrt(2), 1) and \
         normal_3 == Tuple.vector(-1, 1, 0)