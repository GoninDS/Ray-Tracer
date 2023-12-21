# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

# Define a constant for the EPSILON value
EPSILON = 0.00001

# Compares two numbers and determines whether they are equal with a margin of error
def equal(first_value, second_value):
  return abs(first_value - second_value) < EPSILON