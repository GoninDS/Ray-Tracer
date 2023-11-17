# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

from ray_tracer.tuples import Tuple
from ray_tracer.colors import Color
from ray_tracer.gradient_patterns import Gradient_pattern

def test_gradient_pattern():
  pattern = Gradient_pattern(Color.white(), Color.black())
  assert pattern.color_at(Tuple.point(0, 0, 0)) == Color.white() and \
    pattern.color_at(Tuple.point(0.25, 0, 0)) == Color(0.75, 0.75, 0.75) and \
    pattern.color_at(Tuple.point(0.5, 0, 0)) == Color(0.5, 0.5, 0.5) and \
		pattern.color_at(Tuple.point(0.75, 0, 0)) == Color(0.25, 0.25, 0.25)