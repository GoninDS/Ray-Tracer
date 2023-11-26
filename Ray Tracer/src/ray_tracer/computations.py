# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

import math

from ray_tracer.intersections import Intersection
from ray_tracer.colors import Color
from ray_tracer.rays import Ray
import ray_tracer.common as common

class Computation():
  # Default constructor
  def __init__(self):
    self.t = 0
    self.inside = False
    self.shape = None
    self.n1 = None
    self.n2 = None
    self.point = None
    self.eyev = None
    self.normalv = None
    self.reflectv = None
    self.over_point = None
    self.under_point = None

  # Debugging representation
  def __repr__(self):
    return 'Computation()'
  
  # String representation
  def __str__(self): 
    return '({}, {}, {}, {}, {}, {}, {}, {})'.format( \
      self.t, self.shape, self.n1, self.n2, self.point, self.eyev,
      self.normalv, self.reflectv)
  
  # Returns a computations object
  @staticmethod
  def prepare_computations(intersection, ray, intersection_list = None):
    # Create a computations object
    comps = Computation()
    # Get the t and the object from the intersection
    comps.t = intersection.t
    comps.shape = intersection.shape
    # Calculate the point, eye vector and normal vector
    comps.point = ray.position(comps.t)
    comps.eyev = -ray.direction
    comps.normalv = comps.shape.normal_at(comps.point)
    # If the dot product between the normal and the eye vector
    # is less than 0
    if comps.normalv.dot(comps.eyev) < 0:
      # The ray is inside the object and the normal should be reversed
      comps.inside = True
      comps.normalv = -comps.normalv
    # Otherwise
    else:
      # The ray isn't inside the object
      comps.inside = False

    # Calculate the reflect vector
    comps.reflectv = ray.direction.reflect(comps.normalv)
    # Calculate the over and point
    comps.over_point = comps.point + comps.normalv * common.EPSILON
    comps.under_point = comps.point - comps.normalv * common.EPSILON

    # Calculate the refraction points
    if intersection_list is not None:
      comps.calculate_n1_n2(intersection_list, intersection)
    # Return the computations object
    return comps

  def calculate_n1_n2(self, intersection_list, current):
    # Create a list for the containers
    containers = []
    # For to move through all the intersections
    for i in range(len(intersection_list)):
      # If the current intersection is the current
      if intersection_list[i] == current:
        # Set 1.0 or the refractive index of
        # the object as n1
        if len(containers) == 0:
          self.n1 = 1.0
        else:
          self.n1 = containers[-1].material.refractive_index
        
      # If the shape was already in the container
      if intersection_list[i].shape in containers:
        containers.remove(intersection_list[i].shape)
      else:
        containers.append(intersection_list[i].shape)
      
      # If the current intersection is the current
      if intersection_list[i] == current:
        # Set 1.0 or the refractive index of
        # the object as n2
        if len(containers) == 0:
          self.n2 = 1.0
        else:
          self.n2 = containers[-1].material.refractive_index
        return

  # Returns the hit from a list of intersections
  @staticmethod
  def hit(intersections):
    min = None
    for intersection in intersections:
      if (min is None or abs(intersection.t) < min.t):
        min = intersection
    return min
  
  # Calculates the color taking into account the light
  def shade_hit(self, world, remaining_recursions = 4):
    shadowed = world.is_shadowed(self.over_point)
    surface =  world.light.lighting(self.shape, self.point,
      self.eyev, self.normalv, shadowed)
    
    if remaining_recursions != 0:
      reflected = self.reflected_color(world, remaining_recursions)
      if self.n1 is not None and self.n2 is not None:
        refracted = self.refracted_color(world, remaining_recursions)
      else:
        refracted = Color.black()
    else:
      refracted = Color.black()
      reflected = Color.black()

    material = self.shape.material
    if material.reflectiveness > 0 and material.transparency > 0:
      reflectance = self.schlick()
      return surface + reflected * reflectance + refracted * (1 - reflectance)

    return surface + reflected + refracted

  # Calculate the color of a certain point with a given ray
  @staticmethod
  def color_at(world, ray, remaining_recursions = 4):
    # Calculate the intersections in the world
    intersections = ray.intersect_world(world)
    # Obtain the hit from the intersections
    hit = Intersection.hit(intersections)
    # If there is no intersection, return black
    if hit is None:
      return Color.black()
    # If there is an intersection, calculate the values
    else:
      computation = Computation.prepare_computations(hit, ray, intersections)
      return computation.shade_hit(world, remaining_recursions)
  
  # Method to calculate the color of the reflection
  def reflected_color(self, world, remaining_recursions = 4):
    # If the material is partially reflective, return black
    if self.shape.material.reflectiveness == 0 or \
      remaining_recursions <= 0:
      return Color.black()
    
    # Calculate the reflected ray
    reflected_ray = Ray(self.over_point, self.reflectv)
    # Get the color of the reflection
    color = Computation.color_at(world, reflected_ray,
                                 remaining_recursions - 1)
    # Return the color affected by the reflectiveness
    return color * self.shape.material.reflectiveness
  
  # Method to calculate the color of the refraction
  def refracted_color(self, world, remaining_recursions = 4):
    # Find the ratio of the first index of refraction
    n_ratio = self.n1*1.0 / self.n2*1.0
    # Cos theta_i is the same as the dot product of two vectors
    cos_i = self.eyev.dot(self.normalv)
    # Find sin(theta)^2 via trigonometric identity
    sin_t = n_ratio**2 * (1 - (cos_i**2))
    # If the material is not transparent, return black
    if self.shape.material.transparency == 0 or \
      remaining_recursions <= 0 or sin_t > 1:
      return Color.black()
    # Compute the direction of the refracted ray
    cos_t = math.sqrt(1.0 - sin_t)
    direction = self.normalv * (n_ratio * cos_i - cos_t) - self.eyev * n_ratio
    # Create the refracted ray
    refract_ray = Ray(self.under_point, direction)
    color = Computation.color_at(
      world, refract_ray, remaining_recursions - 1) * \
      self.shape.material.transparency

    return color

  def schlick(self):
    # Find the cosine of the angle between
    # the eye and normal vectors
    cos = self.eyev.dot(self.normalv)

    # Total internal reflection can only occur if n1 > n2
    if self.n1 > self.n2:
      n = self.n1 / self.n2
      sin_t = n**2 * (1.0 - cos**2)

      if sin_t > 1.0:
        return 1.0

      # Compute cosine of theta_t using trig identity
      cos_t = math.sqrt(1.0 - sin_t)

      # When n1 > n2, use cos(theta_t) instead
      cos = cos_t
    
    r0 = ((self.n1 - self.n2) / (self.n1 + self.n2))**2
    return r0 + (1 - r0) * (1 - cos)**5