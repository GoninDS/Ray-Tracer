# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

from ray_tracer.canvas import Canvas
from ray_tracer.matrix import Matrix
from ray_tracer.computations import Computation
from ray_tracer.tuples import Tuple
from ray_tracer.rays import Ray
from multiprocessing import Pool, Manager, cpu_count

import math

class Camera:
  def __init__(self, horizontal_size, vertical_size, field_of_view):
    self.horizontal_size = horizontal_size
    self.vertical_size = vertical_size
    self.field_of_view = field_of_view
    self.transformation_matrix = Matrix(4, 4).identity()
    self.calculate_pixel_size()

  def calculate_pixel_size(self):
    # The width of half of the canvas can be computed by taking
    # the tangent of half of the field of view
    self.half_view = math.tan(self.field_of_view / 2)
    # The aspect ratio of the horizontal size of the canvas
    # relative to it's vertical size
    self.aspect = self.horizontal_size / self.vertical_size
    # If the aspect is wide
    if self.aspect >= 1:
      self.half_width = self.half_view
      self.half_height = self.half_view / self.aspect
    # If the aspect is elongated
    else:
      self.half_width = self.half_view * self.aspect
      self.half_height = self.half_view
    # Calculate the pixel size
    self.pixel_size = (self.half_width * 2) / self.horizontal_size

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
  

  @staticmethod
  def process_pixel(camera, world, x, y, shared_data):
    # Create a ray
    ray = camera.ray_for_pixel(x, y)
    # Calculate the color
    color = Computation.color_at(world, ray)

    # Update the shared data with pixel color
    shared_data[(x, y)] = color

  def render_parallel(self, world):
    # Create a shared dictionary to store pixel data
    shared_data = Manager().dict()

    # Create a Pool of processes with the desired number of processes
    with Pool(processes=cpu_count()) as pool:
      # Use a list comprehension to create a list of tuples for the pixel coordinates
      pixels = [(x, y) for y in range(self.vertical_size) for x in range(self.horizontal_size)]

      # Map the process_pixel function to the list of pixel coordinates
      pool.starmap(Camera.process_pixel, [(self, world, x, y, shared_data) for x, y in pixels])

    # Create a canvas using the dimensions of the camera
    image = Canvas(self.horizontal_size, self.vertical_size)

    # Convert the shared dictionary data into the final canvas
    for (x, y), color in shared_data.items():
      image.write_pixel(x, y, color)

    # Return the canvas
    return image
  
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