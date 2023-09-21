# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

from tuples import Tuple

class Matrix:
  # Epsilon constant for comparing two values
  # TODO(Luis & Kenneth): Consider to bring this outside the class to reduce
  # redundancy
  EPSILON = 0.00001

  # Default constructor
  def __init__(self, rows, columns):
    self.mat = \
      [[0.0 for column in range(columns)] for row in range(rows)]
  
  # Creates an invalid matrix instance
  @staticmethod
  def invalid():
    return Matrix(0,0)

  # Debugging representation
  def __repr__(self):
    if not self.is_valid():
      return 'Invalid matrix'
    # Returns how to construct a matrix of the same dimensions
    return 'Matrix({}, {})'.format(len(self.mat), len(self.mat[0]))
  
  # String representation
  def __str__(self):
    # Create an empty string
    matrix_str = ""
    # Move through all the elements in the matrix
    for row in range(len(self.mat)):
      matrix_str += "("
      for column in range(len(self.mat[row])):
        # Add the element to the str
        matrix_str += str(self.mat[row][column])
        # If is not the last element of the row
        if column != len(self.mat[row])-1:
          matrix_str += ",\t\t"
      matrix_str += ")\n"
    # Return the string
    return matrix_str
  
  # Bracket indexation
  def  __getitem__(self, index):
    return self.mat[index]
  
  # Checks if two matrixes are equal in dimensions and values
  def __eq__(self, other):
    # Assume the matrixes won´t be equal
    equal = False
    # If both matrixes are valid
    if self.is_valid() and other.is_valid():
      # If they have the same dimensions
      if len(self.mat) == len(other.mat) \
        and len(self.mat[0]) == len(other.mat[0]):
        # Loop through all the values in the matrixes
        for row in range(len(self.mat)):
          for column in range(len(self.mat[row])):
            # If any two values are not equal
            if not self.equal(self.mat[row][column], other.mat[row][column]):
              # Fail immediately
              return False
        # If it did not fail, change the bool to true
        equal = True
    # If any of the matrixes is invalid
    else:
      # If both matrixes are invalid
      if not self.is_valid() and not other.is_valid():
        equal = True
    # Return the bool
    return equal
  
  # Multiplications
  def __mul__(self, other):
    # If the other is a Color
    if isinstance(other, Matrix):
      return self.matrix_multiplication(other)
    # If the other is int o float
    elif isinstance(other, Tuple):
      return self.tuple_multiplication(other)
     # If other is any other type
    else:
      raise TypeError("Unsupported operand type for multiplication")

  # Matrix multiplication
  def matrix_multiplication(self, other):
    # Both matrixes must be valid and have compatible dimensions
    if not self.is_valid() or not other.is_valid() \
      or not self.have_compatible_dimensions(other):
      return Matrix.invalid()
    # Create an empty new matrix
    new_matrix = Matrix(len(self.mat), len(other.mat[0]))
    # Move through the rows on the first matrix
    for row_self in range(len(self.mat)):
      # Move through the columns on the second matrix
      for column_other in range(len(other.mat[0])):
        # Reset the total
        total = 0
        # Move through the elements on both matrixes
        for element in range(len(self.mat[0])):
          # Multiply the elements and add them to the total
          total += \
            self.mat[row_self][element] * other.mat[element][column_other]
        # Assign the total as the element on the new matrix
        new_matrix.mat[row_self][column_other] = total
    # Return the new matrix
    return new_matrix

  # Matrix-Tuple multiplication
  # TODO(Kenneth): Ask Luis: "The materials says is with vectors
  # but then uses a point as example?"
  # TODO(Kenneth): Ask Luis: "i think we should also have this the other way
  # around vector * self but idk how to implement it without multiple
  # inclusion, help"
  def tuple_multiplication(self, tuple):
     # The matrix mut be valid and have exactly 4 columns
    if not self.is_valid() or len(self.mat[0]) != 4:
      return Matrix.invalid()
    # Create a new tuple
    new_tuple = Tuple()
    # Calculate the values
    new_tuple.x = \
      self.mat[0][0] * tuple.x \
      + self.mat[0][1] * tuple.y \
      + self.mat[0][2] * tuple.z \
      + self.mat[0][3] * tuple.w
    new_tuple.y = \
      self.mat[1][0] * tuple.x \
      + self.mat[1][1] * tuple.y \
      + self.mat[1][2] * tuple.z \
      + self.mat[1][3] * tuple.w
    new_tuple.z = \
      self.mat[2][0] * tuple.x \
      + self.mat[2][1] * tuple.y \
      + self.mat[2][2] * tuple.z \
      + self.mat[2][3] * tuple.w
    new_tuple.w = \
      self.mat[3][0] * tuple.x \
      + self.mat[3][1] * tuple.y \
      + self.mat[3][2] * tuple.z \
      + self.mat[3][3] * tuple.w
    # Return the new tuple
    return new_tuple

  # Returns a submatrix
  # TODO(Luis & Kenneth): Check if this could fail if is not valid
  # also ask the teacher what is the submatrix of a matrix taking away
  # columns and rows it does not have, the same or invalid?
  def submatrix(self, skipping_row, skipping_column):
    # Outside of the valid ranges
    if skipping_row >= len(self.mat) or skipping_column >= len(self.mat[0]):
      return Matrix.invalid()
    # Create a new matrix for the submatrix
    new_matrix = Matrix(len(self.mat) -1, len(self.mat[0])-1)
    # Create indexes to move through the submatrix
    subrow = 0
    subcolumn = 0
    # Move through the rows on the original matrix
    for row in range(len(self.mat)):
      # If is not the row that should be skipped
      if row != skipping_row:
        # Reset the subcolumn
        subcolumn = 0
        # Move through the columns on the original matrix
        for column in range(len(self.mat[0])):
          # If is not the column that should be skipped
          if column != skipping_column:
            # Add the element to the submatrix
            new_matrix.mat[subrow][subcolumn] = self.mat[row][column]
            # Increment the subcolumn
            subcolumn += 1
        # Increment the subrow
        subrow += 1
    # Return the submatrix
    return new_matrix

  # Returns the determinant of the matrix
  # The matrix must be squared and a valid matrix
  def determinant(self):
    rows = len(self.mat)
    columns = len(self.mat[0])
    # Special 1x1 case
    if rows == 1 and columns == 1:
      return self.mat[0][0]
    # Base recursive case (2x2 matrix)
    elif rows == 2 and columns == 2:
      # Calculate the determinant with ad - bc
      return self.mat[0][0] * self.mat[1][1] - self.mat[0][1] * self.mat[1][0]
    # Recursive case
    else:
      # Iterate through the rows and columns of the matrix obtaining the
      # submatrixes to calculate the determinant
      column = 0
      answer = 0
      for row in range(rows):
        # Used to determine the sign of the current value
        value = (-1) ** (row + column) * self.mat[row][column]
        # Calculate the determinant of the submatrix
        answer += value * self.submatrix(row, column).determinant()
      return answer

  # Returns the determinant of a submatrix (minor)
  def minor(self, row, column):
    return self.submatrix(row, column).determinant()

  # Returns the cofactor
  def cofactor(self, row, column):
    if (row + column) % 2 == 0:
      return self.submatrix(row, column).determinant()
    return -self.submatrix(row, column).determinant()

  # Returns the identity matrix
  def identity(self):
    # If the matrix is not valid or it is not squared
    if not self.is_valid() or not self.is_square():
      return Matrix.invalid()
    # Create a new matrix with 0´s
    identity = Matrix(len(self.mat), len(self.mat))
    # Add 1´s to the diagonal
    for diagonal in range(len(self.mat)):
      identity.mat[diagonal][diagonal] = 1
    # Return the identity matrix
    return identity

  # Returns the transpose of the matrix
  def transposing(self):
    # If the matrix is not valid or is not square
    if not self.is_valid() or not self.is_square():
      return Matrix.invalid()
    # Create a new matrix for the transpose
    transpose = Matrix(len(self.mat), len(self.mat))
    # Move through the upper triangle of the matrix
    for row in range(len(self.mat)):
      for column in range(row + 1, len(self.mat[0])):
        # Copy the elements in "transposed" order
        transpose.mat[row][column] = self.mat[column][row]
        transpose.mat[column][row] = self.mat[row][column]
      # Copy the diagonal
      transpose.mat[row][row] = self.mat[row][row]
    # Return the transpose
    return transpose

  # Returns the inverse of the matrix
  def inverse(self):
    if self.is_valid() and self.is_invertible():
      rows = len(self.mat)
      columns = len(self.mat[0])
      # Create an empty new matrix
      new_matrix = Matrix(rows, columns)
      # Calculate the determinant of the original matrix
      determinant = self.determinant()
      for row in range(rows):
        for column in range(columns):
          # Calculate the cofactor of that row and column
          cofactor = self.cofactor(row, column)
          # Calculate the new value in the position [column][row]
          new_matrix.mat[column][row] = cofactor / determinant
      return new_matrix
    # The matrix is invalid or can not be inverted
    return Matrix.invalid()

  # Returns if the two matrixes have compatible dimensions for multiplication
  # Both matrixes must be valid
  def have_compatible_dimensions(self, other):
    return len(self.mat) == len(other.mat[0]) \
      and len(self.mat[0]) == len(other.mat)

  # Returns if the matrix is valid
  def is_valid(self):
    return len(self.mat) != 0 \
      and len(self.mat[0]) != 0
  
  # Returns if the matrix is square
  # The matrix must be valid
  def is_square(self):
    return len(self.mat) == len(self.mat[0])

  # Returns if the matrix is invertible
  # The matrix must be valid
  def is_invertible(self):
    return self.is_square() and self.determinant() != 0
  
  # Checks if two values are basically the same
  # TODO(Luis & Kenneth): Consider to bring this outside the class to reduce
  # redundancy
  def equal(self, first_value, second_value):
    return abs(first_value - second_value) < self.EPSILON