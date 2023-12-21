# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

from ray_tracer.cylinders import Cylinder
from ray_tracer.rays import Ray
from ray_tracer.tuples import Tuple
import ray_tracer.common as common

def test_ray_misses_cylinder():
  cylinder = Cylinder()
  ray_1 = Ray(Tuple.point(1, 0, 0), Tuple.vector(0, 1, 0).normalize())
  ray_2 = Ray(Tuple.point(0, 0, 0), Tuple.vector(0, 1, 0).normalize())
  ray_3 = Ray(Tuple.point(0, 0, -5), Tuple.vector(1, 1, 1).normalize())

  xs_1 = cylinder.local_intersect(ray_1)
  xs_2 = cylinder.local_intersect(ray_2)
  xs_3 = cylinder.local_intersect(ray_3)

  assert len(xs_1) == 0 and \
         len(xs_2) == 0 and \
         len(xs_3) == 0
  
def test_ray_strikes_cylinder():
  cylinder = Cylinder()
  ray_1 = Ray(Tuple.point(1, 0, -5), Tuple.vector(0, 0, 1).normalize())
  ray_2 = Ray(Tuple.point(0, 0, -5), Tuple.vector(0, 0, 1).normalize())
  ray_3 = Ray(Tuple.point(0.5, 0, -5), Tuple.vector(0.1, 1, 1).normalize())

  xs_1 = cylinder.local_intersect(ray_1)
  xs_2 = cylinder.local_intersect(ray_2)
  xs_3 = cylinder.local_intersect(ray_3)

  assert len(xs_1) == 2 and \
            xs_1[0].t == 5 and xs_1[1].t == 5 and \
         len(xs_2) == 2 and \
            xs_2[0].t == 4 and xs_2[1].t == 6 and \
         len(xs_3) == 2 and \
            common.equal(xs_3[0].t, 6.80798) and \
            common.equal(xs_3[1].t, 7.08872)
  
def test_normal_on_cylinder():
  cylinder = Cylinder()
  point_1 = Tuple.point(1, 0, 0)
  point_2 = Tuple.point(0, 5, -1)
  point_3 = Tuple.point(0, -2, 1)
  point_4 = Tuple.point(-1, 1, 0)

  normal_1 = cylinder.local_normal_at(point_1)
  normal_2 = cylinder.local_normal_at(point_2)
  normal_3 = cylinder.local_normal_at(point_3)
  normal_4 = cylinder.local_normal_at(point_4)

  assert normal_1 == Tuple.vector(1, 0, 0) and \
         normal_2 == Tuple.vector(0, 0, -1) and \
         normal_3 == Tuple.vector(0, 0, 1) and \
         normal_4 == Tuple.vector(-1, 0, 0)
  
def test_default_min_and_max_for_cylinder():
  cylinder = Cylinder()
  assert cylinder.minimum == float('-inf') and \
         cylinder.maximum == float('inf')
  
def test_intersect_constrained_cylinder():
  cylinder = Cylinder()
  cylinder.minimum = 1
  cylinder.maximum = 2

  ray_1 = Ray(Tuple.point(0, 1.5, 0), Tuple.vector(0.1, 1, 0).normalize())
  ray_2 = Ray(Tuple.point(0, 3, -5), Tuple.vector(0, 0, 1).normalize())
  ray_3 = Ray(Tuple.point(0, 0, -5), Tuple.vector(0, 0, 1).normalize())
  ray_4 = Ray(Tuple.point(0, 2, -5), Tuple.vector(0, 0, 1).normalize())
  ray_5 = Ray(Tuple.point(0, 1, -5), Tuple.vector(0, 0, 1).normalize())
  ray_6 = Ray(Tuple.point(0, 1.5, -2), Tuple.vector(0, 0, 1).normalize())

  xs_1 = cylinder.local_intersect(ray_1)
  xs_2 = cylinder.local_intersect(ray_2)
  xs_3 = cylinder.local_intersect(ray_3)
  xs_4 = cylinder.local_intersect(ray_4)
  xs_5 = cylinder.local_intersect(ray_5)
  xs_6 = cylinder.local_intersect(ray_6)

  assert len(xs_1) == 0 and \
         len(xs_2) == 0 and \
         len(xs_3) == 0 and \
         len(xs_4) == 0 and \
         len(xs_5) == 0 and \
         len(xs_6) == 2

def test_default_closed_cylinder():
  cylinder = Cylinder()
  assert cylinder.closed == False

def test_intersect_caps_closed_cylinder():
  cylinder = Cylinder()
  cylinder.minimum = 1
  cylinder.maximum = 2
  cylinder.closed = True

  ray_1 = Ray(Tuple.point(0, 3, 0), Tuple.vector(0, -1, 0).normalize())
  ray_2 = Ray(Tuple.point(0, 3, -2), Tuple.vector(0, -1, 2).normalize())
  ray_3 = Ray(Tuple.point(0, 4, -2), Tuple.vector(0, -1, 1).normalize())
  ray_4 = Ray(Tuple.point(0, 0, -2), Tuple.vector(0, 1, 2).normalize())
  ray_5 = Ray(Tuple.point(0, -1, -2), Tuple.vector(0, 1, 1).normalize())

  xs_1 = cylinder.local_intersect(ray_1)
  xs_2 = cylinder.local_intersect(ray_2)
  xs_3 = cylinder.local_intersect(ray_3)
  xs_4 = cylinder.local_intersect(ray_4)
  xs_5 = cylinder.local_intersect(ray_5)

  assert len(xs_1) == 2 and \
         len(xs_2) == 2 and \
         len(xs_3) == 2 and \
         len(xs_4) == 2 and \
         len(xs_5) == 2

def test_normal_on_cylinder_end_caps():
  cylinder = Cylinder()
  cylinder.minimum = 1
  cylinder.maximum = 2
  cylinder.closed = True

  point_1 = Tuple.point(0, 1, 0)
  point_2 = Tuple.point(0.5, 1, 0)
  point_3 = Tuple.point(0, 1, 0.5)
  point_4 = Tuple.point(0, 2, 0)
  point_5 = Tuple.point(0.5, 2, 0)
  point_6 = Tuple.point(0, 2, 0.5)

  normal_1 = cylinder.local_normal_at(point_1)
  normal_2 = cylinder.local_normal_at(point_2)
  normal_3 = cylinder.local_normal_at(point_3)
  normal_4 = cylinder.local_normal_at(point_4)
  normal_5 = cylinder.local_normal_at(point_5)
  normal_6 = cylinder.local_normal_at(point_6)

  assert normal_1 == Tuple.vector(0, -1, 0) and \
         normal_2 == Tuple.vector(0, -1, 0) and \
         normal_3 == Tuple.vector(0, -1, 0) and \
         normal_4 == Tuple.vector(0, 1, 0) and \
         normal_5 == Tuple.vector(0, 1, 0) and \
         normal_6 == Tuple.vector(0, 1, 0)