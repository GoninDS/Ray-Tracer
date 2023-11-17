# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

from ray_tracer.tuples import Tuple
from ray_tracer.colors import Color
from ray_tracer.patterns import Pattern

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

