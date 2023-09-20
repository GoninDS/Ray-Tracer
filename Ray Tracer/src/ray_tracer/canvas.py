# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

from colors import Color

class Canvas:
  # Default constructor
  def __init__(self, height, width):
    self.height = height
    self.width = width
    self.pixels = \
      [[Color.white() for column in range(width)] for row in range(height)]
    
  # Debugging representation
  def __repr__(self):
    # Returns how to construct a canvas of the same dimensions
    return 'Canvas({}, {})'.format(self.height, self.width)
  
  # String representation
  # TODO(Kenneth): Ask Luis if we should print like this or in ppm format
  def __str__(self): 
     # Create an string with the dimensions
    canvas_str = str(self.height) + " " +  str(self.width) + "\n"
    # Move through all the elements in the canvas
    for row in range(self.height):
      for column in range(self.width):
        # Add the element to the str
        canvas_str += str(self.pixels[row][column])
        # If is not the last element of the row
        if column != self.width-1:
          canvas_str += "\t\t"
      canvas_str += "\n"
    # Return the string
    return canvas_str
  
  # Writes a pixel of the specificized color at the given coordinates
  def write_pixel(self, x, y, color):
    self.pixels[x][y] = color

  # Returns the color of the pixel at the given coordinates
  # TODO(Luis & Kenneth): Implement this
  def pixel_at(self, x, y):
    return self.pixels[x][y]

  # Writes a ppm file with the canvas using the specified filename
  # TODO(Luis & Kenneth): Implement this
  def canvas_to_ppm(self, filename):
    pass