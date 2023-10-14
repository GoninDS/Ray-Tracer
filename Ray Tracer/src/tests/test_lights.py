# Copyright Luis Javier Campos Duarte
# Modified by Luis David Solano Santamaría & Kenneth Daniel Villalobos Solís

import pytest
from ray_tracer.lights import Lights
from ray_tracer.tuples import Tuples
from ray_tracer.colors import Colors

def test_point_light_with_intensity_position():
    intensity = Colors(1, 1, 1)
    position = Tuples()
    position = position.Point(0, 0, 0)
    light = Lights()
    light.point_light(position, intensity)
    assert light.position == position
    assert light.intensity == intensity


