# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

from ray_tracer.tuples import Tuple
from ray_tracer.colors import Color
from ray_tracer.lights import Light
from ray_tracer.spheres import Sphere
from ray_tracer.materials import Material
from ray_tracer.transformations import Transformation

class World:
  # Default constructor
  # Sets (0,0,0) as the default point and a black light
  def __init__(self, light = Light(Tuple.point(0, 0, 0), Color.black())):
    # Contains the objects of the world
    self.objects = []
    # Set the light for the world
    self.light = light

  # Create a default world with two spheres, one inside the other
  @staticmethod
  def default_world():
    # Create the light for the default world
    light = Light(Tuple.point(-10, 10, -10), Color.white())
    new_world = World(light)
    # Create the material for the first object
    material = Material(Color(0.8, 1.0, 0.6), 0.1, 0.7, 0.2)
    # Create the first object
    first_sphere = Sphere(material)
    # Insert the object into the world
    new_world.objects.append(first_sphere)
    # Create the second object
    second_sphere = Sphere()
    # Set a transformation to the sphere
    second_sphere.set_transform(Transformation.scaling(0.5, 0.5, 0.5))
    # Insert the object into the world
    new_world.objects.append(second_sphere)
    return new_world
  
  # Debuggin representation
  def __repr__(self):
    return 'World(Light({}, {}))'.format(self.light.position,
      self.light.intensity)
  
  # String representation
  def __str__(self):
    # Insert the light source
    to_str = 'Light({}, {})\n\n\nObjects:\n'.format(self.light.position,
      self.light.intensity)
    # Insert the objects
    for i in range(0, len(self.objects)):
      to_str += str(self.objects[i]) + '\n\n'
    return to_str