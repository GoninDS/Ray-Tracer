# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

from ray_tracer.canvas import Canvas
from ray_tracer.matrix import Matrix
from ray_tracer.computations import Computation
from ray_tracer.tuples import Tuple
from ray_tracer.rays import Ray

class Camera:
  def __init__(self, horizontal_size, vertical_size, field_of_view):
    self.horizontal_size = horizontal_size
    self.vertical_size = vertical_size
    self.field_of_view = field_of_view
    self.transformation_matrix = Matrix.identity()
    self.half_height = 0.0
    self.half_width = 0.0
    self.pixel_size = 0.0

  # Debugging representation
  def __repr__(self):
    return 'Camera({}, {}, {})'.format(\
      self.horizontal_size, self.vertical_size, self.field_of_view)
  
  # String representation
  def __str__(self): 
    return '({}, {}, {}, {})'.format(\
      self.horizontal_size, self.vertical_size, self.field_of_view,
      self.transformation_matrix)

  def ray_for_pixel(self, x_pixel, y_pixel):
    # Calculate an offset from the edge of the pixel's center to the x value
    x_offset = (x_pixel + 0.5) * self.pixel_size
    # Calculate an offset from the edge of the pixel's center to the y value
    y_offset =(y_pixel + 0.5) * self.pixel_size
    # Calculate the x coordinate of the world
    world_x = self.half_width - x_offset
    # Calculate the y coordinate of the world
    world_y = self.half_height - y_offset
    # Transform the canvas point and the origin
    inverse_matrix = self.transformation_matrix.inverse()
    pixel =  inverse_matrix * Tuple.point(world_x, world_y, -1)
    origin = inverse_matrix * Tuple.point(0, 0, 0)
    direction = (pixel - origin).normalize()
    # Return the new ray
    return Ray(origin, direction)

  def render(self, world):
    # Create a canvas using the dimensions of the camera
    image = Canvas(self.horizontal_size, self.vertical_size)
    # For every coordinate on the camera
    for y in range(0, self.vertical_size):
      for x in range(0, self.horizontal_size):
        # Create a ray
        ray = self.ray_for_pixel(x, y)
        # Calculate the color
        color = Computation.color_at(world, ray)
        # Write the pixel on the canvas
        image.write_pixel(x, y, color)
    
    # Return the canvas
    return image