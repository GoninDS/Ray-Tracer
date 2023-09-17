import math

class Tuple:
  # Default constructor
  def __init__(self, x, y, z, w):
    self.x = x
    self.y = y
    self.z = z
    self.w = w

  # Set as vector
  # TODO(Luis & Kenneth): Ask teacher if this constructor should be
  # declared this way
  def vector(self, x, y, z):
    self.__init__(x, y, z, 0)
 
  # Set as point
  # TODO(Luis & Kenneth): Ask teacher if this constructor should be
  # declared this way
  def point(self, x ,y, z):
    self.__init__(x, y, z, 1)

  # Debugging representation
  def __repr__(self):
    return 'Tuple({}, {}, {}, {})'.format(self.x, self.y, self.z, self.w)
  
  # String representation
  def __str__(self): 
    return '({}, {}, {}, {})'.format(self.x, self.y, self.z, self.w)
  
  # Addition of two tuples
  def __add__(self, other):
    new_tuple = Tuple(0, 0, 0, 0)
    new_tuple.x = self.x + other.x
    new_tuple.y = self.y + other.y
    new_tuple.z = self.z + other.z
    new_tuple.w = self.w + other.w
    if new_tuple.w > 1:
      new_tuple.w = 1
    # Return the result
    return new_tuple

  # Subtraction of two tuples
  def __sub__(self, other):
    new_tuple = Tuple(0, 0, 0, 0)
    new_tuple.x = self.x - other.x
    new_tuple.y = self.y - other.y
    new_tuple.z = self.z - other.z
    new_tuple.w = self.w - other.w
    if new_tuple.w < 0:
      new_tuple.w = 0
    # Return the result
    return new_tuple

  # Negation of a tuple
  def __neg__(self):
    self.x = -self.x
    self.y = -self.y
    self.z = -self.z
    # TODO(Luis & Kenneth): Ask if this happens
    # self.w = -self.w

  # Scalar multiplication
  def __mul__(self, scalar):
    self.x *= scalar
    self.y *= scalar
    self.z *= scalar
    self.w *= scalar

  # Scalar division
  def __div__(self, scalar):
    self.x /= scalar
    self.y /= scalar
    self.z /= scalar
    self.w /= scalar

  # Dot product of two tuples
  def dot(self, other):
    result = self.x * other.x
    result += self.y * other.y
    result += self.z * other.z
    result += self.w * other.w
    return result
  
  # Cross product of two tuples
  def cross(self, other):
    new_tuple = Tuple(0, 0, 0, 0)
    new_tuple.x = self.y * other.z - self.z * other.y
    new_tuple.y = self.z * other.x - self.x * self.z
    new_tuple.z = self.x * other.y - self.y * other.z
    # TODO(Luis & Kenneth): Ask if cross product always results in vectors
    return new_tuple

  # Magnitude of a tuple  
  def magnitude(self):
    magnitude = self.x ** 2 + self.y ** 2 + self.z ** 2 + self.w ** 2
    magnitude = math.sqrt(magnitude)
    return magnitude

  # TODO(Luis & Kenneth): consider if static
  # @classmethod
  # @staticmethod
  # Normalization of a tuple
  def normalize(self):
    magnitude = self.magnitude()
    self /= magnitude

  # Returns if the tuple is a vector
  # TODO(Luis & Kenneth): Ask if it is equal or less than zero
  def is_vector(self):
    return self.w <= 0
  
  # Return if the tuple is a point
  # TODO(Luis & Kenneth): Ask if it is equal or greater than zero
  def is_point(self):
    return self.w >= 1