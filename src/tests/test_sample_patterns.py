# Copyright 2023 Luis David Solano Santamaría, Kenneth Daniel Villalobos Solís

from ray_tracer.tuples import Tuple
from ray_tracer.colors import Color
from ray_tracer.sample_patterns import Sample_pattern
from ray_tracer.matrix import Matrix
from ray_tracer.spheres import Sphere
from ray_tracer.transformations import Transformation

def test_sample_pattern_default_transformation():
	pattern = Sample_pattern()
	assert pattern.transform == Matrix(4, 4).identity()

def test_sample_pattern_assign_transformation():
	sphere = Sphere()
	sphere.material.pattern = Sample_pattern()
	sphere.set_pattern_transform(Transformation.translation(1, 2, 3))
	
	assert \
	  sphere.material.pattern.transform == Transformation.translation(1, 2, 3)

def test_sample_pattern_with_transformed_object():
	sphere = Sphere()
	sphere.set_transform(Transformation.scaling(2, 2, 2))
	sphere.material.pattern = Sample_pattern()
	
	color = sphere.color_at(Tuple.point(2, 3, 4))
	assert color == Color(1, 1.5, 2)

def test_sample_material_with_transformation():
  sphere = Sphere()
  sphere.material.pattern = Sample_pattern()
  sphere.set_pattern_transform(Transformation.scaling(2, 2, 2))
	
  color = sphere.color_at(Tuple.point(2, 3, 4))
  assert color == Color(1, 1.5, 2)

def test_transformed_sample_pattern_with_transformed_object():
	sphere = Sphere()
	sphere.set_transform(Transformation.scaling(2, 2, 2))
	sphere.material.pattern = Sample_pattern()
	sphere.set_pattern_transform(Transformation.translation(0.5, 1, 1.5))

	color = sphere.color_at(Tuple.point(2.5, 3, 3.5))
	assert color == Color(0.75, 0.5, 0.25)