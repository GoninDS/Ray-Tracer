class Color:
  # Default constructor
  # TODO(Kenneth): Ask Luis about the name of this attributes
  def __init__(self, r, g, b):
    self.r = r
    self.g = g
    self.b = b

  # Set as the color black
  # TODO(Kenneth): Ask Luis if we should have this constructor
  def black(self):
    self.__init__(0, 0, 0)
 
  # Set as the color white
  # TODO(Kenneth): Ask Luis if we should have this constructor
  def white(self):
    self.__init__(1, 1, 1)

  # Debugging representation
  def __repr__(self):
    return 'Color({}, {}, {})'.format(self.r, self.g, self.b)
  
  # String representation
  def __str__(self): 
    return '({}, {}, {})'.format(self.r, self.g, self.b)
  
  # Adds two colors
  def __add__(self, other):
    new_color = Color(0, 0, 0)
    new_color.r = self.r + other.r
    new_color.g = self.g + other.g
    new_color.b = self.b + other.b
    # Return the result
    return new_color

  # Subtracts two color
  def __sub__(self, other):
    new_color = Color(0, 0, 0)
    new_color.r = self.r - other.r
    new_color.g = self.g - other.g
    new_color.b = self.b - other.b
    # Return the result
    return new_color

  # Negation of a Color
  # TODO(Kenneth): Ask Luis (and possibly the teacher) if we
  # should have this method
  def __neg__(self):
    self.r = -self.r
    self.g = -self.g
    self.b = -self.b

  # Color multiplication
  def __mul__(self, other):
    self.r *= other.r
    self.g *= other.g
    self.b *= other.b

  # Color division
  # TODO(Kenneth): Ask Luis (and possibly the teacher) if we
  # should have this method
  def __div__(self, other):
    self.r /= other.r
    self.g /= other.g
    self.b /= other.b

  # Scalar multiplication
  def __mul__(self, scalar):
    self.r *= scalar
    self.g *= scalar
    self.b *= scalar

  # Scalar division
  # TODO(Kenneth): Ask Luis (and possibly the teacher) if we
  # should have this method
  def __div__(self, scalar):
    self.r /= scalar
    self.g /= scalar
    self.b /= scalar

  # Returns if the tuple is a vector
  # TODO(Kenneth): Ask Luis if we should have this method
  def is_black(self):
    return self.r == 0 and self.g == 0 and self.b == 0
  
  # Return if the tuple is a point
  # TODO(Kenneth): Ask Luis if we should have this method
  def is_white(self):
    return self.r == 1 and self.g == 1 and self.b == 1