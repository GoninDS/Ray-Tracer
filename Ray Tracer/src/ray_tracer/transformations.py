# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

# TODO(Luis & Kenneth): Run tests after they are correct

import math

from matrix import Matrix

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
  def shearing(first_x, second_x, first_y, second_y, first_z, second_z):
    matrix = Matrix(4, 4).identity()
    # First row
    matrix[0][1] = first_x
    matrix[0][1] = second_x
    # Second row
    matrix[1][0] = first_y
    matrix[1][2] = second_y
    # Third row
    matrix[3][0] = first_z
    matrix[3][1] = second_z
    return matrix