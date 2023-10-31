# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

from ray_tracer.colors import Color
from ray_tracer.tuples import Tuple
from ray_tracer.worlds import World
from ray_tracer.lights import Light
from ray_tracer.spheres import Sphere
from ray_tracer.materials import Material
from ray_tracer.transformations import Transformation
from ray_tracer.cameras import Camera
import math


def light_test():
  world = World()

  world.light = Light.point_light(Tuple.point(-10, 100, -10),
                            Color(0.9412, 1, 0.9412))

  floor = Sphere()
  floor.transform = Transformation.scaling(10, 0.01, 10)
  floor.material = Material()
  floor.material.color = Color(1, 1, 1)
  floor.material.specular = 0
  
  left_wall = Sphere()
  left_wall.transform = Transformation.translation(0, 0, 5) * Transformation.rotation_y(-math.pi/4) * Transformation.rotation_x(math.pi/2) * Transformation.scaling(10, 0.01, 10)
  left_wall.material = floor.material
    
  right_wall = Sphere()
  right_wall.transform = Transformation.translation(0, 0, 5) * Transformation.rotation_y(math.pi/4) * Transformation.rotation_x(math.pi/2) * Transformation.scaling(10, 0.01, 10)
  right_wall.material = left_wall.material

  yellow = Sphere()
  yellow.material = Material()
  yellow.material.color = Color(1, 1, 0.4)
  yellow.material.ambient = 0.43301
  yellow.material.diffuse = 0.69282
  yellow.material.specular = 1
  yellow.material.shininess = 76.8
  yellow.transform = Transformation.translation(0, 1, 0)

  green = Sphere()
  green.material = Material()
  green.material.color = Color(0.1333,  0.5451, 0.1333 )
  green.material.ambient = 0.43301
  green.material.diffuse = 0.69282
  green.material.specular = 1
  green.material.shininess = 76.8
  green.transform = Transformation.translation(2.5, 1, 0)

  orange = Sphere()
  orange.material = Material()
  orange.material.color = Color(1, 0.3882, 0.2784)
  orange.material.ambient = 0.43301
  orange.material.diffuse = 0.69282
  orange.material.specular = 1
  orange.material.shininess = 76.8
  orange.transform = Transformation.translation(-2.5, 1, 0)

  world.objects.append(yellow)
  world.objects.append(green)
  world.objects.append(orange)
  world.objects.append(floor)
  world.objects.append(left_wall)
  world.objects.append(right_wall)

  camera = Camera(300, 150, math.pi/3)
  camera.transformation_matrix = Transformation.view_transform(Tuple.point(0, 1, -5),
  Tuple.point(0, 1, 0),
  Tuple.vector(0, 1, 0))

  canvas = camera.render_parallel(world)
  canvas.canvas_to_ppm("cyan_light_test.ppm")

def space():  
  world = World()
    
  world.light = Light.point_light(Tuple.point(-100, 100, -100),
                            Color(1, 1, 1))
    
  earth = Sphere()
  earth.transform = Transformation.translation(-0.5, -1, 0.5) * Transformation.scaling(2, 2, 2)
  earth.material = Material(Color(0.19, 0.40, 0.91), 0, 1, 1, 300)

  mars = Sphere()
  mars.transform = Transformation.translation(-3.5, 1, 10) * Transformation.scaling(1.4, 1.4, 1.4)
  mars.material = Material(Color(0.82, 0.41, 0.12), 0, 1, 0, 300)
  
  moon = Sphere()
  moon.transform = Transformation.translation(1.5, 1, 1.5) * Transformation.scaling(0.7, 0.7, 0.7)
  moon.material = Material(Color(0.33, 0.33, 0.33), 0, 1, 0, 0)
  
  world.objects.append(earth)
  world.objects.append(mars)
  world.objects.append(moon)

  camera = Camera(900, 450, math.pi/3)
  camera.transformation_matrix = Transformation.view_transform(Tuple.point(0, 1.5, -5),
    Tuple.point(0, 1, 0),
    Tuple.vector(0, 1, 0))

  canvas = camera.render_parallel(world)
  canvas.canvas_to_ppm("space_big22.ppm")  

if __name__ == "__main__":
  light_test()