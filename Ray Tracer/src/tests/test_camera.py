import math
import pytest

from ray_tracer.cameras import Camera
from ray_tracer.matrix import Matrix
from ray_tracer.tuples import Tuple
from ray_tracer.transformations import Transformation
from ray_tracer.worlds import World
from ray_tracer.colors import Color
import ray_tracer.common as common

@pytest.fixture
def sample_camera():
  c = Camera(201, 101, math.pi/2)
  return c

def test_constructing_camera():
  hsize = 160
  vsize = 120
  field_of_view = math.pi/2 
  c = Camera(hsize, vsize, field_of_view)
  m = Matrix(4, 4)
  assert common.equals(c.horizontal_size, hsize)
  assert common.equals(c.vertical_size, vsize)
  assert common.equals(c.field_of_view, field_of_view)
  assert c.transformation_matrix == m.identity()
  
def test_pixel_size_horizontal():
  c = Camera(200, 125, math.pi/2)
  assert common.equals(c.pixel_size, 0.01) 
  
def test_pixel_size_vertical():
  c = Camera(125, 200, math.pi/2)
  assert common.equals(c.pixel_size, 0.01)  
  
def test_ray_through_canvas_center(sample_camera):
  r = sample_camera.ray_for_pixel(100, 50)
  assert r.origin == Tuple.point(0, 0, 0)
  assert r.direction == Tuple.vector(0, 0, -1)
  
def test_ray_through_canvas_corner(sample_camera):
  r = sample_camera.ray_for_pixel(0, 0)
  assert r.origin == Tuple.point(0, 0, 0)
  assert r.direction == Tuple.vector(0.66519, 0.33259, -0.66851)
  
def test_ray_through_camera_transformation(sample_camera):
  sample_camera.transformation_matrix = \
    (Transformation.rotation_y(math.pi/4) * \
    Transformation.translation(0, -2, 5))
  r = sample_camera.ray_for_pixel(100, 50)
  assert r.origin == Tuple.point(0, 2, -5)
  assert r.direction == Tuple.vector(math.sqrt(2)/2, 0, -math.sqrt(2)/2)

def test_rendering_world_with_camera():
  w = World.default_world()
  c = Camera(11, 11, math.pi/2)
  pfrom = Tuple.point(0, 0, -5)
  to = Tuple.point(0, 0, 0)
  up = Tuple.vector(0, 1, 0)
  c.transformation_matrix = Transformation.view_transform(pfrom, to, up)
  image = c.render(w)
  color = Color(0.38066, 0.47583, 0.2855) * 255
  color.r = round(color.r)
  color.g = round(color.g)
  color.b = round(color.b)
  assert image.pixel_at(5, 5) == color