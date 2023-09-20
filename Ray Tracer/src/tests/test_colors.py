import pytest

from colors import Color

def test_create_color():
	c = Color(-0.5, 0.4, 1.7)
	assert(c.r == -0.5)
	assert(c.g == 0.4)
	assert(c.b == 1.7)

def test_add_colors():
	c1 = Color(0.9, 0.6, 0.75)
	c2 = Color(0.7, 0.1, 0.25)
	expectedC = Color(1.6, 0.7, 1.0)
	assert(expectedC == c1 + c2)

def test_subtractingColors():
	c1 = Color(0.9, 0.6, 0.75)
	c2 = Color(0.7, 0.1, 0.25)
	expectedC = Color(0.2, 0.5, 0.5)
	assert(expectedC == c1 - c2)

def test_multiplyingColorScalar():
  c1 = Color(0.2, 0.3, 0.4) 
  expectedC = Color(0.4, 0.6, 0.8)
  assert(expectedC == c1 * 2)

def test_multiplyingColors():
  c1 = Color(1, 0.2, 0.4)
  c2 = Color(0.9, 1, 0.1)
  expectedC = Color(0.9, 0.2, 0.04)
  assert(expectedC == c1 * c2)
