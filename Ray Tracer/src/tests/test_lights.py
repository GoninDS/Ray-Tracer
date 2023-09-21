import pytest
from lights import PointLight
from tuples import Tuple
from colors import Color

def test_point_light_with_intensity_position():
  intensity = Color(1, 1, 1)
  position = Tuple.point(0, 0, 0)
  light = PointLight(position, intensity)
  assert light.position == position
  assert light.intensity == intensity


