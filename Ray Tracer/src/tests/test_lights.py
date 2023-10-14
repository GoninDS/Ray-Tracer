# Copyright Luis Javier Campos Duarte
# Modified by Luis David Solano Santamaría & Kenneth Daniel Villalobos Solís

import pytest
from ray_tracer.lights import Light
from ray_tracer.tuples import Tuple
from ray_tracer.colors import Color

def test_point_light_with_intensity_position():
    intensity = Color(1, 1, 1)
    position = Tuple.point(0, 0, 0)
    light = Light(position, intensity)
    assert light.position == position
    assert light.intensity == intensity