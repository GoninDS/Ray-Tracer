# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

from ray_tracer.tuples import Tuple
from ray_tracer.colors import Color
from ray_tracer.ring_patterns import Ring_pattern

def test_ring_extends_in_x_and_y():
  pattern = Ring_pattern(Color.white(), Color.black())
  assert pattern.color_at(Tuple.point(0, 0, 0)) == Color.white() and \
    pattern.color_at(Tuple.point(1, 0, 0)) == Color.black() and \
    pattern.color_at(Tuple.point(0, 0, 1)) == Color.black() and \
    pattern.color_at(Tuple.point(0.708, 0, 0.708)) == Color.black()