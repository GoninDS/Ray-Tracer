# Copyright Luis Javier Campos Duarte
# Modified by Luis David Solano Santamaría & Kenneth Daniel Villalobos Solís

import pytest
from ray_tracer.materials import Material
from ray_tracer.tuples import Tuple
from ray_tracer.colors import Color
from ray_tracer.lights import Light

def test_default_material():
  m = Material()
  color = Color(1, 1, 1)
  assert m.color == color
  assert m.ambient == 0.1
  assert m.diffuse == 0.9
  assert m.specular == 0.9
  assert m.shininess == 200.0

def test_eye_between_light_surface():
  m = Material()
  position = Tuple.point(0, 0, 0)
  eyev = Tuple.vector(0, 0, -1)
  normalv = Tuple.vector(0, 0, -1)
  intensity = Color(1, 1, 1)
  light_position = Tuple.point(0, 0, -10)
  light = Light.point_light(light_position, intensity)
  expected_color = Color(1.9, 1.9, 1.9)
  result = light.lighting(m, position, eyev, normalv)
  assert result == expected_color

def test_light_surface_eye_offset_45():
  m = Material()
  position = Tuple.point(0, 0, 0)
  eyev = Tuple.vector(0, 2**0.5/2, 2**0.5/2)
  normalv = Tuple.vector(0, 0, -1)
  intensity = Color(1, 1, 1)
  light_position = Tuple.point(0, 0, -10)
  light = Light(light_position, intensity)
  expected_color = Color(1.0, 1.0, 1.0)
  result = light.lighting(m, position, eyev, normalv)
  assert result == expected_color

def test_eye_surface_light_offset_45():
  m = Material()
  position = Tuple.point(0, 0, 0)
  eyev = Tuple.vector(0, 0, -1)
  normalv = Tuple.vector(0, 0, -1)
  intensity = Color(1, 1, 1)
  light_position = Tuple.point(0, 10, -10)
  light = Light(light_position, intensity)
  expected_color = Color(0.7364, 0.7364, 0.7364)
  result = light.lighting(m, position, eyev, normalv)
  assert result == expected_color

def test_eye_in_path_of_reflection_vector():
  m = Material()
  position = Tuple.point(0, 0, 0)
  eyev = Tuple.vector(0, -2**0.5/2, -2**0.5/2)
  normalv = Tuple.vector(0, 0, -1)
  intensity = Color(1, 1, 1)
  light_position = Tuple.point(0, 10, -10)
  light = Light(light_position, intensity)
  expected_color = Color(1.6364, 1.6364, 1.6364)
  result = light.lighting(m, position, eyev, normalv)
  assert result == expected_color

def test_light_behind_the_surface():
  m = Material()
  position = Tuple.point(0, 0, 0)
  eyev = Tuple.vector(0, 0, -1)
  normalv = Tuple.vector(0, 0, -1)
  intensity = Color(1, 1, 1)
  light_position = Tuple.point(0, 0, 10)
  light = Light(light_position, intensity)
  expected_color = Color(0.1, 0.1, 0.1)
  result = light.lighting(m, position, eyev, normalv)
  assert result == expected_color