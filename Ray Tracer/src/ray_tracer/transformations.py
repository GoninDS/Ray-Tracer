# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

import math

from ray_tracer.matrix import Matrix

class Transformation():
  # Creates a translation matrix
  @staticmethod
  def translation(translation_x, translation_y, translation_z):
    matrix = Matrix(4, 4).identity()
    matrix[0][3] = translation_x
    matrix[1][3] = translation_y
    matrix[2][3] = translation_z
    return matrix

  # Creates a scaling matrix
  @staticmethod
  def scaling(scaling_x, scaling_y, scaling_z):
    matrix = Matrix(4, 4)
    matrix[0][0] = scaling_x
    matrix[1][1] = scaling_y
    matrix[2][2] = scaling_z
    matrix[3][3] = 1
    return matrix

  # Creates a rotation on x axis matrix
  @staticmethod
  def rotation_x(radians):
    matrix = Matrix(4, 4)
    # First row
    matrix[0][0] = 1
    # Second row
    matrix[1][1] = math.cos(radians)
    matrix[1][2] = -math.sin(radians)
    # Third row
    matrix[2][1] = math.sin(radians)
    matrix[2][2] = math.cos(radians)
    # Fourth row
    matrix[3][3] = 1
    return matrix

  # Creates a rotation on y axis matrix
  @staticmethod
  def rotation_y(radians):
    matrix = Matrix(4, 4)
    # First row
    matrix[0][0] = math.cos(radians)
    matrix[0][2] = math.sin(radians)
    # Second row
    matrix[1][1] = 1
    # Third row
    matrix[2][0] = -math.sin(radians)
    matrix[2][2] = math.cos(radians)
    # Fourth row
    matrix[3][3] = 1
    return matrix

  # Creates a rotation on z axis matrix
  @staticmethod
  def rotation_z(radians):
    matrix = Matrix(4, 4)
    # First row
    matrix[0][0] = math.cos(radians)
    matrix[0][1] = -math.sin(radians)
    # Second row
    matrix[1][0] = math.sin(radians)
    matrix[1][1] = math.cos(radians)
    # Third row
    matrix[2][2] = 1
    # Fourth row
    matrix[3][3] = 1
    return matrix

  # Creates a shearing matrix
  @staticmethod
  def shearing(x_in_y, x_in_z, y_in_x, y_in_z, z_in_x, z_in_y):
    matrix = Matrix(4, 4).identity()
    # First row
    matrix[0][1] = x_in_y
    matrix[0][2] = x_in_z
    # Second row
    matrix[1][0] = y_in_x
    matrix[1][2] = y_in_z
    # Third row
    matrix[2][0] = z_in_x
    matrix[2][1] = z_in_y
    return matrix

# Creates a matrix to transform the camera view
@staticmethod
def view_transform(origin_point, end_point, up_point):
  # Get the forward direction
  forward = (end_point - origin_point).normalize()
  # Normalize the up point
  up_point_normalized = up_point.normalize()
  # Get the left direction
  left = forward.cross(up_point_normalized)
  # Get the true up
  true_up_point = left.cross(forward)

  # Create the orientation matrix
  orientation = Matrix(4, 4)
  # First row
  orientation[0][0] = left.x
  orientation[0][1] = left.y
  orientation[0][2] = left.z
  orientation[0][3] = 0
  # Second row
  orientation[1][0] = true_up_point.x
  orientation[1][1] = true_up_point.y
  orientation[1][2] = true_up_point.z
  orientation[1][3] = 0
  # Third row
  orientation[2][0] = -forward.x
  orientation[2][1] = -forward.y
  orientation[2][2] = -forward.z
  orientation[2][3] = 0
  # Fourth row
  orientation[3][0] = 0
  orientation[3][1] = 0
  orientation[3][2] = 0
  orientation[3][3] = 1

  # Return the orientation applied on the origin
  return orientation * Transformation.translation(-origin_point.x,
    -origin_point.y, -origin_point.z)