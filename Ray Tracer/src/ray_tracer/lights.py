# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

from ray_tracer.colors import Color
from ray_tracer.tuples import Tuple

class Light:
  # Default constructor
  def __init__(self, position, intensity):
    self.position = position
    self.intensity = intensity

  # Create a light pointing at an specific point
  @staticmethod
  def point_light(position, intensity):
    return Light(position, intensity)
  
  # Debugging representation
  def __repr__(self):
    return 'Light(({}, {}, {}), ({}, {}, {}))'.format(
      self.position.x, self.position.y, self.position.z,
      self.intensity.r, self.intensity.g, self.intensity.b)
  
  # String representation
  def __str__(self):
    return '(({}, {}, {}), ({}, {}, {}))'.format(
      self.position.x, self.position.y, self.position.z,
      self.intensity.r, self.intensity.g, self.intensity.b)
  
  # Checks if two light sources are the same
  def __eq__(self, other):
    return self.position == other.position \
      and self.intensity ==  other.intensity
  
  # Calculates the lightning on a point
  def lighting(self, material, point, eyev, normalv, in_shadow=False):
    # If it is not in the shadow
    if in_shadow == False:
      return self.outside_shadow_case(material, point, eyev, normalv)
    # If it is in the shadow
    return self.inside_shadow_case(material)

  # Calculates the lightning for the case outside the shadow
  def outside_shadow_case(self, material, point, eyev, normalv):
    # Calculate the effective color
    effective_color = material.color * self.intensity
    # Calculate the light vector
    lightv = (self.position - point).normalize()
    # Calculate the ambient color
    ambient = effective_color * material.ambient
    # Start the diffuse and specular as black
    diffuse = Color.black()
    specular = Color.black()
    # Calculate the dot product between light vector normal vector
    light_dot_normal = lightv.dot(normalv)
    # If the dot product is more or equal than 0
    if light_dot_normal >= 0:
      # Calculate diffuse
      diffuse = effective_color * material.diffuse * light_dot_normal
      # Calculate the reflect vector and the dot product
      # between the reflect vector and eye vector
      reflectv = (-lightv).reflect(normalv)
      reflect_dot_eye = reflectv.dot(eyev)
      # If the dot product is more than 0
      if reflect_dot_eye > 0:
        # Calculate the specular
        factor = reflect_dot_eye ** material.shininess
        specular = self.intensity * material.specular * factor
    # Returns the lightning
    return ambient + diffuse + specular

  # Calculates the lightning for the case inside the shadow
  def inside_shadow_case(self, material):
    # Calculate the effective color
    effective_color = material.color * self.intensity
    # Calculate the ambient color
    ambient = effective_color * material.ambient
    # Returns the lightning
    return ambient


    
