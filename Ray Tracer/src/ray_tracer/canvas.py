# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

from ray_tracer.colors import Color

class Canvas:
  # Default constructor
  def __init__(self, width, height, color=None):
    # Width for the matrix
    self.width = width
    # Height for the matrix
    self.height = height
    if color is None:
      self.init_none_case()
    else:
      self.init_color_case(color)
    # Used for ppm transfering
    self.character_counter = 0 

  # Modularize none case
  def init_none_case(self):
    self.pixels = []  # Create an empty list to store the pixels
    # Use nested list comprehensions to populate the 2D list
    for row in range(self.height):
      # Create a new row of pixels
      row_pixels = []
      for column in range(self.width):
        # Create a new Color object using the black() method and translate it to the canvas
        color = Color.black().translate_to_canvas()
        # Append the color to the row
        row_pixels.append(color)
      # Append the row to the main list
      self.pixels.append(row_pixels)

  # Modularize color case
  def init_color_case(self, color):
    # Translate the color to canvas format
    color = color.translate_to_canvas()
    # Create an empty list to store the pixels
    self.pixels = []
    # Use nested list comprehensions to populate the 2D list
    for row in range(self.height):
      # Create a new row of pixels
      row_pixels = []
      for column in range(self.width):
        # Create a new Color object and append it to the row
        row_pixels.append(Color(color.r, color.g, color.b))
      # Append the row to the main list
      self.pixels.append(row_pixels)
  
  # Debugging representation
  def __repr__(self):
    # Returns how to construct a canvas of the same dimensions
    return 'Canvas({}, {})'.format(self.height, self.width)
  
  # String representation
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
    # Translate the color in a 255 range to store it
    self.pixels[y][x] = color.translate_to_canvas()

  # Returns the color of the pixel at the given coordinates
  def pixel_at(self, x, y):
    print(self.pixels[y][x])
    return self.pixels[y][x]

  # Writes a ppm file with the canvas using the specified filename
  def canvas_to_ppm(self, filename):
    # Open a file with the truncate option
    file = open(filename, 'w')
    self.write_ppm_header(file)
    self.write_ppm_body(file)

  # Writes the header of the file
  def write_ppm_header(self, file):
    # Write the format
    file.write('P3\n')
    # Write the x and y dimensions
    file.write('{} {}'.format(self.width, self.height))
    file.write('\n')
    # Write the max value possible in the PPM file
    file.write('255\n')

  # Writes the contents of the file
  def write_ppm_body(self, file):
    # Variables for method implementation
    self.character_counter = 0
    # Go through the matrix
    for row in range(self.height):
      for column in range(self.width):
        # Write in the file for the red value
        self.write_color(self.pixels[row][column].r, file)
        # Write in the file for the green value
        self.write_color(self.pixels[row][column].g, file)
        # Write in the file for the blue value
        self.write_color(self.pixels[row][column].b, file)
      # Write a new line
      file.write('\n')
      # Reset character counter
      self.character_counter = 0

  def write_color(self, value, file):
    # Round the value to an integer
    value = round(value)
    # Check if the value overflows the maximum
    if (value > 255):
      value = 255
    # Turn the value into a string
    string_value = str(value)
    # Update the character counter
    self.character_counter += len(string_value) + 1
    # Check if the line overflows
    if (self.character_counter > 70):
      string_value = '\n' + string_value + ' '
      self.character_counter = len(string_value) + 1
    else:
      # There is no overboard, leave a space
      string_value = string_value + ' '
    # Write the contents to the file
    file.write(string_value)