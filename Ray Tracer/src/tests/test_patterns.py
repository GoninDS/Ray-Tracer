# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

from ray_tracer.tuples import Tuple
from ray_tracer.colors import Color
from ray_tracer.patterns import Pattern
from ray_tracer.materials import Material
from ray_tracer.lights import Light

def test_striped_pattern():
  pattern = Pattern.striped_pattern(Color.white(), Color.black())
  assert pattern.first_color == Color.white() and \
    pattern.second_color == Color.black()

def test_constant_striped_pattern_y():
	pattern = Pattern.striped_pattern(Color.white(), Color.black())
	assert pattern.stripe_at(Tuple.point(0, 0, 0)) == Color.white() and \
    pattern.stripe_at(Tuple.point(0, 1, 0)) == Color.white() and \
		pattern.stripe_at(Tuple.point(0, 2, 0)) == Color.white()

def test_constant_striped_pattern_z():
	pattern = Pattern.striped_pattern(Color.white(), Color.black())
	assert pattern.stripe_at(Tuple.point(0, 0, 0)) == Color.white() and \
    pattern.stripe_at(Tuple.point(0, 0, 1)) == Color.white() and \
		pattern.stripe_at(Tuple.point(0, 0, 2)) == Color.white()

def test_alternates_striped_pattern_x():
	pattern = Pattern.striped_pattern(Color.white(), Color.black())
	assert pattern.stripe_at(Tuple.point(0, 0, 0)) == Color.white() and \
    pattern.stripe_at(Tuple.point(0.9, 0, 0)) == Color.white() and \
    pattern.stripe_at(Tuple.point(1, 0, 0)) == Color.black() and \
    pattern.stripe_at(Tuple.point(-0.1, 0, 0)) == Color.black() and \
    pattern.stripe_at(Tuple.point(-1, 0, 0)) == Color.black() and \
    pattern.stripe_at(Tuple.point(-1.1, 0, 0)) == Color.white()

def test_lighting_with_patter():
	material = Material()
	material.pattern = Pattern.striped_pattern(Color(1, 1, 1), Color(0, 0, 0))
	material.ambient = 1
	material.diffuse = 0
	material.specular = 0

	eyev = Tuple.vector(0, 0, -1)
	normalv = Tuple.vector(0, 0, -1)
	light = Light.point_light(Tuple.point(0, 0, -10), Color(1, 1, 1))
	color1 = \
		light.lighting(material, Tuple.point(0.9, 0, 0), eyev, normalv, False)
	color2 = \
		light.lighting(material, Tuple.point(1.1, 0, 0), eyev, normalv, False)

	assert color1 == Color(1, 1, 1) and color2 == Color(0, 0, 0)

def text


Scenario: Stripes with an object transformation
Given object ← sphere()
And set_transform(object, scaling(2, 2, 2))
And pattern ← stripe_pattern(white, black)
When c ← stripe_at_object(pattern, object, point(1.5, 0, 0))
Then c = white

Scenario: Stripes with a pattern transformation
Given object ← sphere()
And pattern ← stripe_pattern(white, black)
And set_pattern_transform(pattern, scaling(2, 2, 2))
When c ← stripe_at_object(pattern, object, point(1.5, 0, 0))
Then c = white

Scenario: Stripes with both an object and a pattern transformation
Given object ← sphere()
And set_transform(object, scaling(2, 2, 2))
And pattern ← stripe_pattern(white, black)
And set_pattern_transform(pattern, translation(0.5, 0, 0))
When c ← stripe_at_object(pattern, object, point(2.5, 0, 0))
Then c = white
