# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

from ray_tracer.tuples import Tuple
from ray_tracer.colors import Color
from ray_tracer.striped_patterns import Striped_pattern
from ray_tracer.materials import Material
from ray_tracer.lights import Light
from ray_tracer.spheres import Sphere
from ray_tracer.transformations import Transformation

def test_striped_pattern():
  pattern = Striped_pattern(Color.white(), Color.black())
  assert pattern.first_color == Color.white() and \
    pattern.second_color == Color.black()

def test_constant_striped_pattern_y():
	pattern = Striped_pattern(Color.white(), Color.black())
	assert pattern.color_at(Tuple.point(0, 0, 0)) == Color.white() and \
    pattern.color_at(Tuple.point(0, 1, 0)) == Color.white() and \
		pattern.color_at(Tuple.point(0, 2, 0)) == Color.white()

def test_constant_striped_pattern_z():
	pattern = Striped_pattern(Color.white(), Color.black())
	assert pattern.color_at(Tuple.point(0, 0, 0)) == Color.white() and \
    pattern.color_at(Tuple.point(0, 0, 1)) == Color.white() and \
		pattern.color_at(Tuple.point(0, 0, 2)) == Color.white()

def test_alternates_striped_pattern_x():
	pattern = Striped_pattern(Color.white(), Color.black())
	assert pattern.color_at(Tuple.point(0, 0, 0)) == Color.white() and \
    pattern.color_at(Tuple.point(0.9, 0, 0)) == Color.white() and \
    pattern.color_at(Tuple.point(1, 0, 0)) == Color.black() and \
    pattern.color_at(Tuple.point(-0.1, 0, 0)) == Color.black() and \
    pattern.color_at(Tuple.point(-1, 0, 0)) == Color.black() and \
    pattern.color_at(Tuple.point(-1.1, 0, 0)) == Color.white()

def test_lighting_with_striped_pattern():
	sphere = Sphere()
	sphere.material = Material()
	sphere.material.pattern = Striped_pattern(Color(1, 1, 1), Color(0, 0, 0))
	sphere.material.ambient = 1
	sphere.material.diffuse = 0
	sphere.material.specular = 0

	eyev = Tuple.vector(0, 0, -1)
	normalv = Tuple.vector(0, 0, -1)
	light = Light.point_light(Tuple.point(0, 0, -10), Color(1, 1, 1))
	color1 = \
		light.lighting(sphere, Tuple.point(0.9, 0, 0), eyev, normalv, False)
	color2 = \
		light.lighting(sphere, Tuple.point(1.1, 0, 0), eyev, normalv, False)

	assert color1 == Color(1, 1, 1) and color2 == Color(0, 0, 0)

def test_stripes_with_transformed_object():
	sphere = Sphere()
	sphere.set_transform(Transformation.scaling(2, 2, 2))
	sphere.material.pattern = Striped_pattern(Color.white(), Color.black())

	color = sphere.color_at(Tuple.point(1.5, 0, 0))
	assert color == Color.white()

def test_stripes_with_pattern_transformation():
	sphere = Sphere()
	sphere.material.pattern = \
		Striped_pattern(Color.white(), Color.black())
	sphere.set_pattern_transform(Transformation.scaling(2, 2, 2))
	
	color = sphere.color_at(Tuple.point(1.5, 0, 0))
	assert color == Color.white()

def test_stripes_with_object_and_pattern_transformation():
	sphere = Sphere()
	sphere.material.pattern = \
		Striped_pattern(Color.white(), Color.black())
	sphere.set_transform(Transformation.scaling(2, 2, 2))
	sphere.set_pattern_transform(Transformation.translation(0.5, 0, 0))
	
	color = sphere.color_at(Tuple.point(2.5, 0, 0))
	assert color == Color.white()