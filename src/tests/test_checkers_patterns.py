# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

from ray_tracer.tuples import Tuple
from ray_tracer.colors import Color
from ray_tracer.checkers_patterns import Checkers_pattern
from ray_tracer.spheres import Sphere  

def test_checkers_repeats_in_x():
  pattern = Checkers_pattern(Color.white(), Color.black())
  assert pattern.color_at(Tuple.point(0, 0, 0)) == Color.white() and \
    pattern.color_at(Tuple.point(0.99, 0, 0)) == Color.white() and \
    pattern.color_at(Tuple.point(1.01, 0, 0)) == Color.black()

def test_checkers_repeats_in_y():
  pattern = Checkers_pattern(Color.white(), Color.black())
  assert pattern.color_at(Tuple.point(0, 0, 0)) == Color.white() and \
    pattern.color_at(Tuple.point(0, 0.99, 0)) == Color.white() and \
    pattern.color_at(Tuple.point(0, 1.01, 0)) == Color.black()

def test_checkers_repeats_in_z():
  pattern = Checkers_pattern(Color.white(), Color.black())
  assert pattern.color_at(Tuple.point(0, 0, 0)) == Color.white() and \
    pattern.color_at(Tuple.point(0, 0, 0.99)) == Color.white() and \
    pattern.color_at(Tuple.point(0, 0, 1.01)) == Color.black()