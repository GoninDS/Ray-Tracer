# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

class Color:
  EPSILON = 0.00001

  # Default constructor
  def __init__(self, r = 1.0, g = 1.0, b = 1.0):
    self.r = r
    self.g = g
    self.b = b

  # Create a black instance
  @staticmethod
  def black():
    return Color(0.0, 0.0, 0.0)
 
  # Create a white instance
  @staticmethod
  def white():
    return Color(1.0, 1.0, 1.0)

  # Debugging representation
  def __repr__(self):
    return 'Color({}, {}, {})'.format(self.r, self.g, self.b)
  
  # String representation
  def __str__(self): 
    return '({}, {}, {})'.format(self.r, self.g, self.b)
  
  # Checks if two colors are equal in values
  def __eq__(self, other):
    return self.equal(self.r, other.r) and \
    self.equal(self.g, other.g) and \
    self.equal(self.b, other.b)

  # Addition of two colors
  def __add__(self, other):
    new_color = Color()
    new_color.r = self.r + other.r
    new_color.g = self.g + other.g
    new_color.b = self.b + other.b
    # Return the result
    return new_color

  # Subtraction of two colors
  def __sub__(self, other):
    new_color = Color()
    new_color.r = self.r - other.r
    new_color.g = self.g - other.g
    new_color.b = self.b - other.b
    # Return the result
    return new_color

  # Negation of a Color
  def __neg__(self):
    negated_color = Color()
    negated_color.r = -self.r
    negated_color.g = -self.g
    negated_color.b = -self.b
    return negated_color
  
  # Multiplications
  def __mul__(self, other):
    # If the other is a Color
    if isinstance(other, Color):
      return self.color_multiplication(other)
    # If the other is int o float
    elif isinstance(other, (int, float)):
      return self.scalar_multiplication(other)
     # If other is any other type
    else:
      raise TypeError("Unsupported operand type for multiplication")

  # Color multiplication
  def color_multiplication(self, other):
    result = Color()
    result.r = self.r * other.r
    result.g = self.g * other.g
    result.b = self.b * other.b
    return result
  
  # Scalar multiplication
  def scalar_multiplication(self, scalar):
    result = Color()
    result.r = self.r * scalar
    result.g = self.g * scalar
    result.b = self.b * scalar
    return result
  
  # Divisions
  def __truediv__(self, other):
    # If the other is a Color
    if isinstance(other, Color):
      return self.color_division(other)
    # If the other is int o float
    elif isinstance(other, (int, float)):
      return self.scalar_division(other)
    # If other is any other type
    else:
      raise TypeError("Unsupported operand type for division")

  # Color division
  def color_division(self, other):
    result = Color()
    result.r = self.r / other.r
    result.g = self.g / other.g
    result.b = self.b / other.b
    return result

  # Scalar division
  def scalar_division(self, scalar):
    result = Color()
    result.r = self.r / scalar
    result.g = self.g / scalar
    result.b = self.b / scalar
    return result

  # Returns if the tuple is a vector
  def is_black(self):
    return self.r == 0.0 and self.g == 0.0 and self.b == 0.0
  
  # Return if the tuple is a point
  def is_white(self):
    return self.r == 1.0 and self.g == 1.0 and self.b == 1.0

  # Checks if two values are basically the same
  def equal(self, first_value, second_value):
    return abs(first_value - second_value) < self.EPSILON