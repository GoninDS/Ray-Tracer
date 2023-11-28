import math
import pytest

from ray_tracer.cubes import Cube
from ray_tracer.rays import Ray
from ray_tracer.tuples import Tuple
from ray_tracer.transformations import Transformation
from ray_tracer.worlds import World
from ray_tracer.colors import Color
import ray_tracer.common as common

def test_ray_intersects_cube():
  cube = Cube()
  ray_positive_x = Ray(Tuple.point(5, 0.5, 0), Tuple.vector(-1, 0, 0))
  ray_negative_x = Ray(Tuple.point(-5, 0.5, 0), Tuple.vector(1, 0, 0))
  ray_positive_y = Ray(Tuple.point(0.5, 5, 0), Tuple.vector(0, -1, 0))
  ray_negative_y = Ray(Tuple.point(0.5, -5, 0), Tuple.vector(0, 1, 0))
  ray_positive_z = Ray(Tuple.point(0.5, 0, 5), Tuple.vector(0, 0, -1))
  ray_negative_z = Ray(Tuple.point(0.5, 0, -5), Tuple.vector(0, 0, 1))
  ray_inside = Ray(Tuple.point(0, 0.5, 0), Tuple.vector(0, 0, 1))

  xs_positive_x = cube.local_intersect(ray_positive_x)
  xs_negative_x = cube.local_intersect(ray_negative_x)
  xs_positive_y = cube.local_intersect(ray_positive_y)
  xs_negative_y = cube.local_intersect(ray_negative_y)
  xs_positive_z = cube.local_intersect(ray_positive_z)
  xs_negative_z = cube.local_intersect(ray_negative_z)
  xs_inside = cube.local_intersect(ray_inside)

  assert len(xs_positive_x) == 2 and \
    xs_positive_x[0].t == 4 and xs_positive_x[1].t == 6 and \
    len(xs_negative_x) == 2 and \
    xs_negative_x[0].t == 4 and xs_negative_x[1].t == 6 and \
    len(xs_positive_y) == 2 and \
    xs_positive_y[0].t == 4 and xs_positive_y[1].t == 6 and \
    len(xs_negative_y) == 2 and \
    xs_negative_y[0].t == 4 and xs_negative_y[1].t == 6 and \
    len(xs_positive_z) == 2 and \
    xs_positive_z[0].t == 4 and xs_positive_z[1].t == 6 and \
    len(xs_negative_z) == 2 and \
    xs_negative_z[0].t == 4 and xs_negative_z[1].t == 6 and \
    len(xs_inside) == 2 and \
    xs_inside[0].t == -1 and xs_inside[1].t == 1
  
def test_ray_misses_cube():
  cube = Cube()
  ray_1 = Ray(Tuple.point(-2, 0, 0), Tuple.vector(0.2673, 0.5345, 0.8018))
  ray_2 = Ray(Tuple.point(0, -2, 0), Tuple.vector(0.8018, 0.2673, 0.5345))
  ray_3 = Ray(Tuple.point(0, 0, -2), Tuple.vector(0.5345, 0.8018, 0.2673))
  ray_4 = Ray(Tuple.point(2, 0, 1), Tuple.vector(0, 0, -1))
  ray_5 = Ray(Tuple.point(0, 2, 2), Tuple.vector(0, -1, 0))
  ray_6 = Ray(Tuple.point(2, 2, 0), Tuple.vector(-1, 0, 0))

  xs_1 = cube.local_intersect(ray_1)
  xs_2 = cube.local_intersect(ray_2)
  xs_3 = cube.local_intersect(ray_3)
  xs_4 = cube.local_intersect(ray_4)
  xs_5 = cube.local_intersect(ray_5)
  xs_6 = cube.local_intersect(ray_6)

  assert len(xs_1) == 0 and \
         len(xs_2) == 0 and \
         len(xs_3) == 0 and \
         len(xs_4) == 0 and \
         len(xs_5) == 0 and \
         len(xs_6) == 0
  
def test_normal_on_cube():
  cube = Cube()
  point_1 = Tuple.point(1, 0.5, -0.8)
  point_2 = Tuple.point(-1, -0.2, 0.9)
  point_3 = Tuple.point(-0.4, 1, -0.1)
  point_4 = Tuple.point(0.3, -1, -0.7)
  point_5 = Tuple.point(-0.6, 0.3, 1)
  point_6 = Tuple.point(0.4, 0.4, -1)
  point_7 = Tuple.point(1, 1, 1)
  point_8 = Tuple.point(-1, -1, -1)

  normal_1 = cube.local_normal_at(point_1)
  normal_2 = cube.local_normal_at(point_2)
  normal_3 = cube.local_normal_at(point_3)
  normal_4 = cube.local_normal_at(point_4)
  normal_5 = cube.local_normal_at(point_5)
  normal_6 = cube.local_normal_at(point_6)
  normal_7 = cube.local_normal_at(point_7)
  normal_8 = cube.local_normal_at(point_8)

  assert normal_1 == Tuple.vector(1, 0, 0) and \
         normal_2 == Tuple.vector(-1, 0, 0) and \
         normal_3 == Tuple.vector(0, 1, 0) and \
         normal_4 == Tuple.vector(0, -1, 0) and \
         normal_5 == Tuple.vector(0, 0, 1) and \
         normal_6 == Tuple.vector(0, 0, -1) and \
         normal_7 == Tuple.vector(1, 0, 0) and \
         normal_8 == Tuple.vector(-1, 0, 0)