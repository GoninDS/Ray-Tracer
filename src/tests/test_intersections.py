# Copyright Luis Javier Campos Duarte
# Modified by Luis David Solano Santamaría & Kenneth Daniel Villalobos Solís

import math

from ray_tracer.worlds import World
from ray_tracer.spheres import Sphere
from ray_tracer.planes import Plane
from ray_tracer.intersections import Intersection
from ray_tracer.computations import Computation
from ray_tracer.transformations import Transformation
from ray_tracer.tuples import Tuple
from ray_tracer.rays import Ray
from ray_tracer.colors import Color
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

def test_find_various_intersections():
  a = Sphere.glass_sphere()
  a.transform = Transformation.scaling(2, 2, 2)
  b = Sphere.glass_sphere()
  b.transform = Transformation.translation(0, 0, -0.25)
  b.material.refractive_index = 2.0
  c = Sphere.glass_sphere()
  c.transform = Transformation.translation(0, 0, 0.25)
  c.material.refractive_index = 2.5

  ray = Ray(Tuple.point(0, 0, -4), Tuple.vector(0, 0, 1))
  xs = [Intersection(2, a), Intersection(2.75, b), Intersection(3.25, c),
        Intersection(4.75, b), Intersection(5.25, c), Intersection(6, a)]

  comps_0 = Computation.prepare_computations(xs[0], ray, xs)
  comps_1 = Computation.prepare_computations(xs[1], ray, xs)
  comps_2 = Computation.prepare_computations(xs[2], ray, xs)
  comps_3 = Computation.prepare_computations(xs[3], ray, xs)
  comps_4 = Computation.prepare_computations(xs[4], ray, xs)
  comps_5 = Computation.prepare_computations(xs[5], ray, xs)

  assert comps_0.n1 == 1.0 and comps_0.n2 == 1.5 and \
    comps_1.n1 == 1.5 and comps_1.n2 == 2.0 and \
    comps_2.n1 == 2.0 and comps_2.n2 == 2.5 and \
    comps_3.n1 == 2.5 and comps_3.n2 == 2.5 and \
    comps_4.n1 == 2.5 and comps_4.n2 == 1.5 and \
    comps_5.n1 == 1.5 and comps_5.n2 == 1.0

def test_prepare_computations_calculates_under_point():
  ray = Ray(Tuple.point(0, 0, -5), Tuple.vector(0, 0, 1))
  shape = Sphere.glass_sphere()
  shape.transform = Transformation.translation(0, 0, 1)
  intersection = Intersection(5, shape)
  xs = []
  xs.append(intersection)
  comps = Computation.prepare_computations(intersection, ray, xs)
  assert comps.under_point.z > common.EPSILON/2 and \
         comps.point.z < comps.under_point.z

def test_schlick_aprox_under_internal_reflection():
  shape = Sphere.glass_sphere()
  ray = Ray(Tuple.point(0, 0, math.sqrt(2)/2), Tuple.vector(0, 1, 0))
  xs = [Intersection(-math.sqrt(2)/2, shape),
        Intersection(math.sqrt(2)/2, shape)]
  comps = Computation.prepare_computations(xs[1], ray, xs)
  reflectance = comps.schlick()
  assert reflectance == 1.0

def test_schlick_aprox_perpendicular_viewing_angle():
  shape = Sphere.glass_sphere()
  ray = Ray(Tuple.point(0, 0, 0), Tuple.vector(0, 1, 0))
  xs = [Intersection(-1, shape), Intersection(1, shape)]
  comps = Computation.prepare_computations(xs[1], ray, xs)
  reflectance = comps.schlick()
  assert common.equal(reflectance, 0.04)

def test_schlick_approximation_with_small_angle_and_n2_bigger():
  shape = Sphere.glass_sphere()
  ray = Ray(Tuple.point(0, 0.99, -2), Tuple.vector(0, 0, 1))
  xs = [Intersection(1.8589, shape)]
  comps = Computation.prepare_computations(xs[0], ray, xs)
  reflectance = comps.schlick()
  assert common.equal(reflectance, 0.48873)

def test_shade_hit_with_reflective_transparent_material():
  world = World.default_world()
  ray = Ray(Tuple.point(0, 0, -3),
            Tuple.vector(0, -math.sqrt(2)/2, math.sqrt(2)/2))
  floor = Plane()
  floor.transform = Transformation.translation(0, -1, 0)
  floor.material.reflectiveness = 0.5
  floor.material.transparency = 0.5
  floor.material.refractive_index = 1.5
  world.objects.append(floor)

  ball = Sphere()
  ball.material.color = Color(1, 0, 0)
  ball.material.ambient = 0.5
  ball.transform = Transformation.translation(0, -3.5, -0.5)
  world.objects.append(ball)

  xs = [Intersection(math.sqrt(2), floor)]
  comps = Computation.prepare_computations(xs[0], ray, xs)
  color = comps.shade_hit(world, 5)
  assert color == Color(0.93391, 0.69643, 0.69243)