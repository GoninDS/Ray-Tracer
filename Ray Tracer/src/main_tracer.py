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

def main():  
  world = World()
    
  world.light = Light.point_light(Tuple.point(-10, 10, -10),
                            Color(1, 1, 1))
    
  floor = Sphere()
  floor.transform = Transformation.scaling(10, 0.01, 10)
  floor.material = Material()
  floor.material.color = Color(1, 0.9, 0.9)
  floor.material.specular = 0
  
  left_wall = Sphere()
  left_wall.transform = Transformation.translation(0, 0, 5) * Transformation.rotation_y(-math.pi/4) * Transformation.rotation_x(math.pi/2) * Transformation.scaling(10, 0.01, 10)
  left_wall.material = floor.material
    
  right_wall = Sphere()
  right_wall.transform = Transformation.translation(0, 0, 5) * Transformation.rotation_y(math.pi/4) * Transformation.rotation_x(math.pi/2) * Transformation.scaling(10, 0.01, 10)
  right_wall.material = floor.material
    
  middle = Sphere()
  middle.transform = Transformation.translation(-0.5, 1, 0.5)
  middle.material = Material()
  middle.material.color = Color(0.1, 1, 0.5)
  middle.material.diffuse = 0.7
  middle.material.specular = 0.3
    
  right = Sphere()
  right.transform = Transformation.translation(1.5, 0.5, -0.5) * Transformation.scaling(0.5, 0.5, 0.5)
  right.material = Material()
  right.material.color = Color(0.5, 1, 0.1)
  right.material.diffuse = 0.7
  right.material.specular = 0.3
    
  left = Sphere()
  left.transform = Transformation.translation(-1.5, 0.33, -0.75) * Transformation.scaling(0.33, 0.33, 0.33)
  left.material = Material()
  left.material.color = Color(1, 0.8, 0.1)
  left.material.diffuse = 0.7
  left.material.specular = 0.3
    
  world.objects.append(floor)
  world.objects.append(left_wall) 
  world.objects.append(right_wall)
  world.objects.append(middle)
  world.objects.append(right)
  world.objects.append(left)

  camera = Camera(300, 150, math.pi/3)
  camera.transformation_matrix = Transformation.view_transform(Tuple.point(0, 1.5, -5),
    Tuple.point(0, 1, 0),
    Tuple.vector(0, 1, 0))

  canvas = camera.render(world)
  canvas.canvas_to_ppm("purpleCircle2.ppm")  

if __name__ == "__main__":
  main()