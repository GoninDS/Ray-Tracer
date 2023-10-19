# Copyright Luis Javier Campos Duarte
# Modified by Luis David Solano Santamaría & Kenneth Daniel Villalobos Solís

import pytest
from ray_tracer.worlds import World
from ray_tracer.rays import Ray
from ray_tracer.spheres import Sphere
from ray_tracer.intersections import Intersection
from ray_tracer.computations import Computation
from ray_tracer.tuples import Tuple
from ray_tracer.colors import Color
from ray_tracer.lights import Light
from ray_tracer.materials import Material
from ray_tracer.transformations import Transformation

def test_creating_world():
  world = World()
  assert len(world.objects) == 0

def test_creating_default_world():
  world = World.default_world()

  point = Tuple.point(-10, 10, -10)
  color = Color(1, 1, 1)
  light = Light.point_light(point, color)

  material = Material()
  material.color = Color(0.8, 1.0, 0.6)
  material.diffuse = 0.7
  material.specular = 0.2

  s1 = Sphere()
  s1.material = material
  s1.id = world.objects[0].id

  s2 = Sphere()
  s2.set_transform(Transformation.scaling(0.5, 0.5, 0.5))
  s2.id = world.objects[1].id

  assert world.light == light
  assert s1 in world.objects
  assert s2 in world.objects

def test_intersect_world_ray():
  world = World.default_world()

  origin = Tuple.point(0, 0, -5)
  direction = Tuple.vector(0, 0, 1)
  ray = Ray(origin, direction)

  xs = ray.intersect_world(world)

  assert len(xs) == 4
  assert xs[0].t == 4
  assert xs[1].t == 4.5
  assert xs[2].t == 5.5
  assert xs[3].t == 6

def test_shading_intersection():
  world = World.default_world()

  origin = Tuple.point(0, 0, -5)
  direction = Tuple.vector(0, 0, 1)
  ray = Ray(origin, direction)

  shape = world.objects[0]

  i = Intersection(4, shape)
  comps = Computation.prepare_computations(i, ray)
  c = comps.shade_hit(world.light)
  col = Color(0.38066, 0.47583, 0.2855)
  print(str(c))
  print(str(col))
  assert c == col

def test_shading_intersection_inside():
  world = World.default_world()

  point = Tuple.point(0, 0.25, 0)
  color = Color(1, 1, 1)
  l = Light(point, color)
  world.light = l

  origin = Tuple.point(0, 0, 0)
  direction = Tuple.vector(0, 0, 1)
  ray = Ray(origin, direction)

  shape = world.objects[1]

  i = Intersection(0.5, shape)
  comps = Computation.prepare_computations(i, ray)
  c = comps.shade_hit(world.light)
  col = Color(0.90498, 0.90498, 0.90498)

  assert c == col

def test_color_ray_misses():
  world = World.default_world()

  origin = Tuple.point(0, 0, -5)
  direction = Tuple.vector(0, 1, 0)
  ray = Ray(origin, direction)

  c = Computation.color_at(world, ray)
  col = Color(0, 0, 0)

  assert c == col

def test_color_ray_hits():
  world = World.default_world()

  origin = Tuple.point(0, 0, -5)
  direction = Tuple.vector(0, 0, 1)
  ray = Ray(origin, direction)

  c = Computation.color_at(world, ray)
  col = Color(0.38066, 0.47583, 0.2855)

  assert c == col

def test_color_intersection_behind_ray():
  world = World.default_world()

  outer = world.objects[0]
  outer.material.ambient = 1

  inner = world.objects[1]
  inner.material.ambient = 1

  origin = Tuple.point(0, 0, 0.75)
  direction = Tuple.vector(0, 0, -1)
  ray = Ray(origin, direction)

  c = Computation.color_at(world, ray)

  assert c == inner.material.color