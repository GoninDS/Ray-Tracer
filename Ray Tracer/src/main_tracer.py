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
  space()