# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

import ray_tracer.common as common

class Intersection():
  # Default constructor
  def __init__(self, t, object):
    self.t = t
    self.object = object

  # Debugging representation
  def __repr__(self):
    return 'Intersection({}, {})'.format(self.t, self.object)
  
  # String representation
  def __str__(self): 
    return '({}, {})'.format(self.t, self.object)
  
  # Checks if two intersections are equal
  def __eq__(self, other):
    return common.equal(self.t, other.t) and \
      self.object.id == other.object.id
  
  # Method to return the value of the t
  # Used for sorting
  @staticmethod
  def value_t(intersection):
    return intersection.t

  # Returns the hit from a list of intersections
  @staticmethod
  def intersections(*intersections):
    result = list(intersections)
    result.sort(key=Intersection.value_t)
    return result

  # Orders all the intersections in a list
  @staticmethod
  def list_intersections(intersections):
    intersections.sort(key=Intersection.value_t)
    return intersections

  # Returns the hit from a list of intersections
  @staticmethod
  def hit(intersections):
    min = None
    for intersection in intersections:
      if (intersection.t >= 0 and (min is None or intersection.t < min.t)):
        min = intersection
    return min