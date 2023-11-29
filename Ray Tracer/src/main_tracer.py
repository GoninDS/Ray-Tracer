# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

from ray_tracer.colors import Color
from ray_tracer.tuples import Tuple
from ray_tracer.worlds import World
from ray_tracer.lights import Light
from ray_tracer.spheres import Sphere
from ray_tracer.materials import Material
from ray_tracer.transformations import Transformation
from ray_tracer.cameras import Camera
from ray_tracer.checkers_patterns import Checkers_pattern
from ray_tracer.cubes import Cube
from ray_tracer.planes import Plane
from ray_tracer.striped_patterns import Striped_pattern
from ray_tracer.ring_patterns import Ring_pattern
from ray_tracer.cylinders import Cylinder

import math


def pikachu():
  world = World()
    
  world.light = Light.point_light(Tuple.point(-10, 10, -10),
                            Color(1, 1, 1))
    
  floor = Sphere()
  floor.transform = Transformation.scaling(10, 0.01, 10)
  floor.material = Material()
  floor.material.color = Color(0.2, 0.8, 0.2)
  floor.material.specular = 0
  
  left_wall = Sphere()
  left_wall.transform = Transformation.translation(0, 0, 5) * Transformation.rotation_y(-math.pi/4) * Transformation.rotation_x(math.pi/2) * Transformation.scaling(10, 0.01, 10)
  left_wall.material = Material(Color(0.68, 0.85, 0.9), 1, 0, 0, 200)
    
  right_wall = Sphere()
  right_wall.transform = Transformation.translation(0, 0, 5) * Transformation.rotation_y(math.pi/4) * Transformation.rotation_x(math.pi/2) * Transformation.scaling(10, 0.01, 10)
  right_wall.material = left_wall.material
    
  body = Sphere()
  body.transform = Transformation.translation(-0.5, 0.5, 0.5) * Transformation.scaling(0.5, 0.5, 0.5)
  body.material = Material(Color(1, 0.902, 0.176), 0.3, 0.6, 0, 50)

  head = Sphere()
  head.transform = Transformation.translation(-0.5, 1.2, 0.5) * Transformation.scaling(0.3, 0.3, 0.3)
  head.material = Material(Color(1, 0.902, 0.176), 0.3, 0.6, 0, 50)

  right_paw = Sphere()
  right_paw.transform = Transformation.translation(-0.2, 0.1, 0.5) * Transformation.scaling(0.2, 0.1, 0.4)
  right_paw.material = Material(Color(1, 0.902, 0.176), 0.3, 0.6, 0, 50)

  left_paw = Sphere()
  left_paw.transform = Transformation.translation(-0.8, 0.1, 0.5) * Transformation.scaling(0.2, 0.1, 0.4)
  left_paw.material = Material(Color(1, 0.902, 0.176), 0.3, 0.6, 0, 50)

  right_arm = Sphere()
  right_arm.transform = Transformation.translation(-0.3, 0.75, 0.3) * Transformation.scaling(0.2, 0.1, 0.4)
  right_arm.material = Material(Color(1, 0.902, 0.176), 0.3, 0.6, 0, 50)

  left_arm = Sphere()
  left_arm.transform = Transformation.translation(-0.7, 0.75, 0.3) * Transformation.scaling(0.2, 0.1, 0.4)
  left_arm.material = Material(Color(1, 0.902, 0.176), 0.3, 0.6, 0, 50)

  right_ear = Sphere()
  right_ear.transform = Transformation.translation(0, 1.4, 0.5) * Transformation.rotation_z((math.pi *3) / 2) * Transformation.scaling(0.1, 0.4, 0.1)
  right_ear.material = Material(Color(1, 0.902, 0.176), 0.3, 0.6, 0, 50)

  left_ear = Sphere()
  left_ear.transform = Transformation.translation(-0.8, 1.6, 0.5) * Transformation.rotation_z(math.pi / 4) * Transformation.scaling(0.1, 0.4, 0.1)
  left_ear.material = Material(Color(1, 0.902, 0.176), 0.3, 0.6, 0, 50)

  tail_base = Sphere()
  tail_base.transform = Transformation.translation(0, 0.5, 0.8) * Transformation.scaling(0.4, 0.1, 0.01)
  tail_base.material = Material(Color(1, 0.902, 0.176), 0.3, 0.6, 0, 50)

  tail_body = Sphere()
  tail_body.transform = Transformation.translation(0.5, 0.9, 0.8) * Transformation.scaling(0.12, 0.4, 0.01) * Transformation.shearing(1, 0, 0, 0, 0, 0)
  tail_body.material = Material(Color(1, 0.902, 0.176), 0.3, 0.6, 0, 50)

  tail_tip = Sphere()
  tail_tip.transform = Transformation.translation(0.86, 1.3, 0.8) * Transformation.scaling(0.4, 0.2, 0.01)
  tail_tip.material = Material(Color(1, 0.902, 0.176), 0.3, 0.6, 0, 50)

  left_eye = Sphere()
  left_eye.transform = Transformation.translation(-0.39, 1.4, -1.1) * Transformation.scaling(0.025, 0.025, 0.01)
  left_eye.material = Material(Color.black(), 0, 0, 1, 200)

  right_eye = Sphere()
  right_eye.transform = Transformation.translation(-0.3, 1.4, -1.1) * Transformation.scaling(0.025, 0.025, 0.001)
  right_eye.material = Material(Color.black(), 0, 0, 1, 200)

  left_cheek = Sphere()
  left_cheek.transform = Transformation.translation(-0.45, 1.3, -1.0) * Transformation.scaling(0.025, 0.025, 0.01)
  left_cheek.material = Material(Color(0.91, 0.16, 0.16), 0.3, 0.6, 0, 50)

  right_cheek = Sphere()
  right_cheek.transform = Transformation.translation(-0.25, 1.3, -1.0) * Transformation.scaling(0.025, 0.025, 0.001)
  right_cheek.material = Material(Color(0.91, 0.16, 0.16), 0.3, 0.6, 0, 50)
    
  world.objects.append(floor)
  world.objects.append(left_wall) 
  world.objects.append(right_wall)
  world.objects.append(body)
  world.objects.append(head)
  world.objects.append(right_paw)
  world.objects.append(left_paw)
  world.objects.append(right_arm)
  world.objects.append(left_arm)
  world.objects.append(right_ear)
  world.objects.append(left_ear)
  world.objects.append(tail_base)
  world.objects.append(tail_body)
  world.objects.append(tail_tip)
  world.objects.append(left_eye)
  world.objects.append(right_eye)
  world.objects.append(left_cheek)
  world.objects.append(right_cheek)

  camera = Camera(300, 150, math.pi/3)
  camera.transformation_matrix = Transformation.view_transform(Tuple.point(0, 1.5, -5),
    Tuple.point(0, 1, 0),
    Tuple.vector(0, 1, 0))

  canvas = camera.render_parallel(world)
  canvas.canvas_to_ppm("pikachu43.ppm")  

def light_test():
  world = World()

  world.light = Light.point_light(Tuple.point(-10, 100, -10),
                            Color(0.2941, 0, 0.5098))

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
  canvas.canvas_to_ppm("purple_light_test.ppm")

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

def transparent_sphere():
  world = World()
  world.light = Light.point_light(Tuple.point(-10, 100, -10),
                            Color(1, 1, 1))

  shape = Sphere()
  shape.material = Material(Color(1, 1, 1))
  shape.material.reflectiveness = 0.8
  shape.material.transparency = 0.5
  shape.material.refractive_index = 1.0
  shape.material.shininess = 200
  shape.material.diffuse = 0.1
  shape.material.specular = 0.9
  shape.transform = Transformation.translation(0, 1, 0)

  second_shape = Sphere()
  second_shape.material = Material(Color(0, 0, 1))
  second_shape.transform = Transformation.translation(0, 1, 15)

  plane = Plane()
  plane.material.specular = 0
  plane.material.pattern = Checkers_pattern(Color(0.35, 0.35, 0.35), Color(0.65, 0.65, 0.65))
  
  camera = Camera(300, 300, math.pi/3)
  camera.transformation_matrix =  Transformation.view_transform(Tuple.point(0, 1, -5),
  Tuple.point(0, 1, 0),
  Tuple.vector(0, 1, 0))
  
  world.objects.append(shape)
  world.objects.append(second_shape)
  world.objects.append(plane)

  canvas = camera.render_parallel(world)
  canvas.canvas_to_ppm("transparent_sphere_5.ppm")

def reflective_sphere():
  world = World()
  world.light = Light.point_light(Tuple.point(-10, 100, -10),
                            Color(1, 1, 1))
  
  shape = Sphere()
  shape.material = Material(Color(0.8, 0.8, 0.8))
  shape.material.reflectiveness = 0.8
  shape.material.transparency = 0.0
  shape.material.refractive_index = 1.0
  shape.material.shininess = 200
  shape.material.diffuse = 0.1
  shape.material.specular = 0.9
  shape.transform = Transformation.translation(0, 1, 0)

  plane = Plane()
  plane.material.specular = 0
  plane.material.pattern = Checkers_pattern(Color(0.35, 0.35, 0.35), Color(0.65, 0.65, 0.65))

  second_shape = Sphere()
  second_shape.material = Material(Color(0, 0, 1))
  second_shape.transform = Transformation.translation(0, 1, -15)

  third_shape = Sphere()
  third_shape.material = Material(Color(1, 0, 0))
  third_shape.transform = Transformation.translation(-5, 1, -5)

  fourth_shape = Sphere()
  fourth_shape.material = Material(Color(0, 1, 0))
  fourth_shape.transform = Transformation.translation(0, 5, -9)

  fifth_shape = Sphere()
  fifth_shape.material = Material(Color(0.38, 0.871, 0.851))
  fifth_shape.transform = Transformation.translation(-4, 5, -9)

  sixth_shape = Sphere()
  sixth_shape.material = Material(Color(0.541, 0.384, 0.871))
  sixth_shape.transform = Transformation.translation(8, 1, 0)

  camera = Camera(1000, 1000, math.pi/3)
  camera.transformation_matrix =  Transformation.view_transform(Tuple.point(0, 1, -5),
  Tuple.point(0, 1, 0),
  Tuple.vector(0, 1, 0))
  
  world.objects.append(shape)
  world.objects.append(second_shape)
  world.objects.append(third_shape)
  world.objects.append(fourth_shape)
  world.objects.append(fifth_shape)
  world.objects.append(sixth_shape)
  world.objects.append(plane)

  canvas = camera.render_parallel(world)
  canvas.canvas_to_ppm("reflective_sphere.ppm")


def reflective_floor_test():
  world = World()
  world.light = Light.point_light(Tuple.point(-4.9, 4.9, -1), Color(1, 1, 1))

  plane = Plane()
  plane.material.reflectiveness = 0.4
  plane.material.specular = 0
  plane.material.pattern = Checkers_pattern(Color(0.35, 0.35, 0.35), Color(0.65, 0.65, 0.65))
  plane.material.pattern.transform = Transformation.rotation_y(90)

  first_sphere = Sphere()
  first_sphere.material.color = Color(0, 0, 1)
  first_sphere.transform = Transformation.translation(0, 0, 5)

  second_sphere = Sphere()
  second_sphere.material.color = Color(1, 0, 0)
  second_sphere.transform = Transformation.translation(2.5, 0 , 5)

  third_sphere = Sphere()
  third_sphere.material.color = Color(0, 1, 0)
  third_sphere.transform = Transformation.translation(-2.5, 0 , 5)

  camera = Camera(1500, 1000, math.pi/3)
  camera.transformation_matrix =  Transformation.view_transform(Tuple.point(0, 1, -5),
  Tuple.point(0, 1, 0),
  Tuple.vector(0, 1, 0))

  world.objects.append(plane)
  world.objects.append(first_sphere)
  world.objects.append(second_sphere)
  world.objects.append(third_sphere)

  canvas = camera.render_parallel(world)
  canvas.canvas_to_ppm("reflective_floor_10.ppm")

if __name__ == "__main__":
  reflective_sphere()