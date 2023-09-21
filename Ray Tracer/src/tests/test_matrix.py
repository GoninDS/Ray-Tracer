import pytest

from matrix import Matrix
from tuples import Tuple

COLUMNS = 4
ROWS = 4

def test_constructing_matrix():
	matrix = Matrix(4, 4)
	value = 1
	for row in range(ROWS):
		for column in range(COLUMNS):			
			matrix.mat[row][column] = value
			value += 1
		value += 0.5
		if (row == 1):
			value += -1
	assert(1 == matrix.mat[0][0])
	assert(4 == matrix.mat[0][3])
	assert(5.5 == matrix.mat[1][0])
	assert(7.5 == matrix.mat[1][2])
	assert(11 == matrix.mat[2][2])
	assert(13.5 == matrix.mat[3][0])
	assert(15.5 == matrix.mat[3][2])

def test_constructing_inspecting_a():
  matrix = Matrix(2, 2)
  matrix.mat[0][0] = -3
  matrix.mat[0][1] = 5
  matrix.mat[1][0] = 1
  matrix.mat[1][1] = -2
  assert(-3 == matrix.mat[0][0])
  assert(5 == matrix.mat[0][1])
  assert(1 == matrix.mat[1][0])
  assert(-2 == matrix.mat[1][1])

def test_constructing_inspecting_b():
	matrix = Matrix(3, 3)
	matrix.mat[0][0] = -3
	matrix.mat[0][1] = 5
	matrix.mat[0][2] = 0
	matrix.mat[1][0] = 1
	matrix.mat[1][1] = -2
	matrix.mat[1][2] = -7
	matrix.mat[2][0] = 0
	matrix.mat[2][1] = 1
	matrix.mat[2][2] = 1
	assert(-3 == matrix.mat[0][0])
	assert(-2 == matrix.mat[1][1])
	assert(1 == matrix.mat[2][2])

def test_matrix_identical():
  A = Matrix(4, 4)
  B = Matrix(4, 4)
  value = 1
  diff = 2
  for row in range(ROWS):
    for column in range(COLUMNS):
      if (value < 10):
        A.mat[row][column] = B.mat[row][column] = value
        value += 1
      else:
        A.mat[row][column] = B.mat[row][column] = value - diff
        diff += -1
  assert(A == B)

def test_matrix_difference():
  A = Matrix(4, 4)
  B = Matrix(4, 4)
  value = 1
  diff = 2 
  value2 = 2
  for row in range(ROWS):
    for column in range(COLUMNS):
      if (value < 10):
        A.mat[row][column] = value
        B.mat[row][column] = value2
        value += 1
        value2 += 1
      else:
        A.mat[row][column] = value - diff
        B.mat[row][column] = value2 - diff
        diff += 1
  assert not (A == B)

def multiplyingTwoMatrices():
  A = Matrix(4, 4)
  B = Matrix(4, 4)
  C = Matrix(4, 4)
  value = 1
  diff = 2
  for row in range(ROWS):
    for column in range(COLUMNS):
      if (value < 10):
        A.mat[row][column] = value
        value += 1
      else:
        A.mat[row][column] = value - diff
        diff += 1
              
  B.mat[0][0] = -2
  B.mat[0][1] = 1
  B.mat[0][2] = 2
  B.mat[0][3] = 3
  B.mat[1][0] = 3
  B.mat[1][1] = 2
  B.mat[1][2] = 1
  B.mat[1][3] = -1
  B.mat[2][0] = 4
  B.mat[2][1] = 3
  B.mat[2][2] = 6
  B.mat[2][3] = 5
  B.mat[3][0] = 1
  B.mat[3][1] = 2
  B.mat[3][2] = 7
  B.mat[3][3] = 8
  
  C.mat[0][0] = 20
  C.mat[0][1] = 22
  C.mat[0][2] = 50
  C.mat[0][3] = 48
  C.mat[1][0] = 4
  C.mat[1][1] = 54
  C.mat[1][2] = 114
  C.mat[1][3] = 108
  C.mat[2][0] = 40
  C.mat[2][1] = 58
  C.mat[2][2] = 110
  C.mat[2][3] = 102
  C.mat[3][0] = 16
  C.mat[3][1] = 26
  C.mat[3][2] = 46
  C.mat[3][3] = 42
  assert(C == (A*B))

def multiplyingMatrixTuple():
  A = Matrix(4, 4)
  B = Tuple(1, 2, 3, 1)
  expected = Tuple(18, 24, 33, 1)
  A.mat[0][0] = 1
  A.mat[0][1] = 2
  A.mat[0][2] = 3
  A.mat[0][3] = 4
  
  A.mat[1][0] = 2
  A.mat[1][1] = 4
  A.mat[1][2] = 4
  A.mat[1][3] = 2
  
  A.mat[2][0] = 8
  A.mat[2][1] = 6
  A.mat[2][2] = 4
  A.mat[2][3] = 1
  
  A.mat[3][0] = 0
  A.mat[3][1] = 0
  A.mat[3][2] = 0
  A.mat[3][3] = 1
  
  assert(expected == (A*B))

def multiplyingMatrixIdentity():
  A = Matrix(4, 4)

  A.mat[0][0] = 0
  A.mat[0][1] = 1
  A.mat[0][2] = 2
  A.mat[0][3] = 4

  A.mat[1][0] = 1
  A.mat[1][1] = 2
  A.mat[1][2] = 4
  A.mat[1][3] = 8

  A.mat[2][0] = 2
  A.mat[2][1] = 4
  A.mat[2][2] = 8
  A.mat[2][3] = 16

  A.mat[3][0] = 4
  A.mat[3][1] = 8
  A.mat[3][2] = 16
  A.mat[3][3] = 32

  assert(A == (A*A.identity()))

def multiplyingIndetityTuple():
  A = Tuple(1, 2, 3, 4)
  m = Matrix(A) # This will create an empty matrix with 4 columns and 1 row

  assert(A == (m.identity()*A))

def transposingMatrix():
  A = Matrix(4, 4)
  expected = Matrix(4, 4)
  
  A.mat[0][0] = 0
  A.mat[0][1] = 9
  A.mat[0][2] = 3
  A.mat[0][3] = 0
  
  A.mat[1][0] = 9
  A.mat[1][1] = 8
  A.mat[1][2] = 0
  A.mat[1][3] = 8
  
  A.mat[2][0] = 1
  A.mat[2][1] = 8
  A.mat[2][2] = 5
  A.mat[2][3] = 3
  
  A.mat[3][0] = 0
  A.mat[3][1] = 0
  A.mat[3][2] = 5
  A.mat[3][3] = 8
  
  expected.mat[0][0] = 0
  expected.mat[0][1] = 9
  expected.mat[0][2] = 1
  expected.mat[0][3] = 0
  
  expected.mat[1][0] = 9
  expected.mat[1][1] = 8
  expected.mat[1][2] = 8
  expected.mat[1][3] = 0
  
  expected.mat[2][0] = 3
  expected.mat[2][1] = 0
  expected.mat[2][2] = 5
  expected.mat[2][3] = 5
  
  expected.mat[3][0] = 0
  expected.mat[3][1] = 8
  expected.mat[3][2] = 3
  expected.mat[3][3] = 8
  assert(expected == A.transposing())

def transposingIdentity():
  m = Matrix(4, 4)
  A = m.identity().transposing()

  assert(A == m.identity())

def determinant2x2():
  m = Matrix(2, 2)
  m.mat[0][0] = 1
  m.mat[0][1] = 5
  m.mat[1][0] = -3
  m.mat[1][1] = 2
  assert(17 == m.determinant())

def submatrix1():
  a = Matrix(3, 3)
  b = Matrix(2, 2)
  a.mat[0][0] = 1
  a.mat[0][1] = 5
  a.mat[0][2] = 0
  
  a.mat[1][0] = -3
  a.mat[1][1] = 2
  a.mat[1][2] = 7
  
  a.mat[2][0] = 0
  a.mat[2][1] = 6
  a.mat[2][2] = -3
  
  b.mat[0][0] = -3
  b.mat[0][1] = 2
  
  b.mat[1][0] = 0
  b.mat[1][1] = 6
  assert(b == a.submatrix(a, 0, 2))

def submatrix2():
  a = Matrix(4, 4)
  b = Matrix(3, 3)
  
  a.mat[0][0] = -6
  a.mat[0][1] = 1
  a.mat[0][2] = 1
  a.mat[0][3] = 6
  
  a.mat[1][0] = -8
  a.mat[1][1] = 5
  a.mat[1][2] = 8
  a.mat[1][3] = 6
  
  a.mat[2][0] = -1
  a.mat[2][1] = 0
  a.mat[2][2] = 8
  a.mat[2][3] = 2
  
  a.mat[3][0] = -7
  a.mat[3][1] = 1
  a.mat[3][2] = -1
  a.mat[3][3] = 1
  
  b.mat[0][0] = -6
  b.mat[0][1] = 1
  b.mat[0][2] = 6
  
  b.mat[1][0] = -8
  b.mat[1][1] = 8
  b.mat[1][2] = 6
  
  b.mat[2][0] = -7
  b.mat[2][1] = -1
  b.mat[2][2] = 1
  
  assert(b == a.submatrix(a, 2, 1))

def minor3x3():
  a = Matrix(3, 3)
  
  a.mat[0][0] = 3
  a.mat[0][1] = 5
  a.mat[0][2] = 0
  
  a.mat[1][0] = 2
  a.mat[1][1] = -1
  a.mat[1][2] = -7
  
  a.mat[2][0] = 6
  a.mat[2][1] = -1
  a.mat[2][2] = 5
  
  b = a.submatrix(a, 1, 0)
  assert(b.determinant() == 25)
  assert(a.minor(a, 1, 0) == 25)

def cofactor3x3():
	a = Matrix(3, 3)

	a.mat[0][0] = 3
	a.mat[0][1] = 5
	a.mat[0][2] = 0

	a.mat[1][0] = 2
	a.mat[1][1] = -1
	a.mat[1][2] = -7

	a.mat[2][0] = 6
	a.mat[2][1] = -1
	a.mat[2][2] = 5

	assert(a.minor(a, 0, 0) == -12)
	assert(a.cofactor(a, 0, 0) == -12)
	assert(a.minor(a, 1, 0) == 25)
	assert(a.cofactor(a, 1, 0) == -25)

def cofactor3x3V2():
	a = Matrix(3, 3)

	a.mat[0][0] = 1
	a.mat[0][1] = 2
	a.mat[0][2] = 6

	a.mat[1][0] = -5
	a.mat[1][1] = 8
	a.mat[1][2] = -4

	a.mat[2][0] = 2
	a.mat[2][1] = 6
	a.mat[2][2] = 4

	assert(a.cofactor(a, 0, 0) == 56)
	assert(a.cofactor(a, 0, 1) == 12)
	assert(a.cofactor(a, 0, 2) == -46)
	assert(a.determinant() == -196)

def cofactor4x4():
	a = Matrix(4, 4)

	a.mat[0][0] = -2
	a.mat[0][1] = -8
	a.mat[0][2] = 3
	a.mat[0][3] = 5

	a.mat[1][0] = -3
	a.mat[1][1] = 1
	a.mat[1][2] = 7
	a.mat[1][3] = 3

	a.mat[2][0] = 1
	a.mat[2][1] = 2
	a.mat[2][2] = -9
	a.mat[2][3] = 6

	a.mat[3][0] = -6
	a.mat[3][1] = 7
	a.mat[3][2] = 7
	a.mat[3][3] = -9

	assert(a.cofactor(a, 0, 0) == 690)
	assert(a.cofactor(a, 0, 1) == 447)
	assert(a.cofactor(a, 0, 2) == 210)
	assert(a.cofactor(a, 0, 3) == 51)
	assert(a.determinant() == -4071)

def isInvertible1():
	a = Matrix(4, 4)

	a.mat[0][0] = 6
	a.mat[0][1] = 4
	a.mat[0][2] = 4
	a.mat[0][3] = 4

	a.mat[1][0] = 5
	a.mat[1][1] = 5
	a.mat[1][2] = 7
	a.mat[1][3] = 6

	a.mat[2][0] = 4
	a.mat[2][1] = -9
	a.mat[2][2] = 3
	a.mat[2][3] = -7

	a.mat[3][0] = 9
	a.mat[3][1] = 1
	a.mat[3][2] = 7
	a.mat[3][3] = -6

	assert(a.determinant() == -2120)
	assert(a.isInvertible())

def isInvertible2():
	a = Matrix(4, 4)

	a.mat[0][0] = -4
	a.mat[0][1] = 2
	a.mat[0][2] = -2
	a.mat[0][3] = -3

	a.mat[1][0] = 9
	a.mat[1][1] = 6
	a.mat[1][2] = 2
	a.mat[1][3] = 6

	a.mat[2][0] = 0
	a.mat[2][1] = -5
	a.mat[2][2] = 1
	a.mat[2][3] = -5

	a.mat[3][0] = 0
	a.mat[3][1] = 0
	a.mat[3][2] = 0
	a.mat[3][3] = 0

	assert(a.determinant() == 0)
	assert not(a.isInvertible())

def invertMatrix1():
  a = Matrix(4, 4)
  expected = Matrix(4, 4)
  
  a.mat[0][0] = -5
  a.mat[0][1] = 2
  a.mat[0][2] = 6
  a.mat[0][3] = -8
  
  a.mat[1][0] = 1
  a.mat[1][1] = -5
  a.mat[1][2] = 1
  a.mat[1][3] = 8
  
  a.mat[2][0] = 7
  a.mat[2][1] = 7
  a.mat[2][2] = -6
  a.mat[2][3] = -7
  
  a.mat[3][0] = 1
  a.mat[3][1] = -3
  a.mat[3][2] = 7
  a.mat[3][3] = 4
  
  expected.mat[0][0] = 0.21805
  expected.mat[0][1] = 0.45113
  expected.mat[0][2] = 0.24060
  expected.mat[0][3] = -0.04511
  
  expected.mat[1][0] = -0.80827
  expected.mat[1][1] = -1.45677
  expected.mat[1][2] = -0.44361
  expected.mat[1][3] = 0.52068
  
  expected.mat[2][0] = -0.07895
  expected.mat[2][1] = -0.22368
  expected.mat[2][2] = -0.05263
  expected.mat[2][3] = 0.19737
  
  expected.mat[3][0] = -0.52256
  expected.mat[3][1] = -0.81391
  expected.mat[3][2] = -0.30075
  expected.mat[3][3] = 0.30639
  
  b = a.inverse(a)
  assert(a.determinant() == 532)
  assert(a.cofactor(a, 2, 3) == -160)
  assert(b.mat[3][2], -160/532)
  assert(a.cofactor(a, 3, 2) == 105)
  assert(b.mat[2][3] == 105/532)
  assert(expected == b)	

def invertMatrix2():
  a = Matrix(4, 4)
  expected = Matrix(4, 4)
  
  a.mat[0][0] = 8
  a.mat[0][1] = -5
  a.mat[0][2] = 9
  a.mat[0][3] = 2
  
  a.mat[1][0] = 7
  a.mat[1][1] = 5
  a.mat[1][2] = 6
  a.mat[1][3] = 1
  
  a.mat[2][0] = -6
  a.mat[2][1] = 0
  a.mat[2][2] = 9
  a.mat[2][3] = 6
  
  a.mat[3][0] = -3
  a.mat[3][1] = 0
  a.mat[3][2] = -9
  a.mat[3][3] = -4
  
  expected.mat[0][0] = -0.15385
  expected.mat[0][1] = -0.15385
  expected.mat[0][2] = -0.28205
  expected.mat[0][3] = -0.53846
  
  expected.mat[1][0] = -0.07692
  expected.mat[1][1] = 0.12308
  expected.mat[1][2] = 0.02564
  expected.mat[1][3] = 0.03077
  
  expected.mat[2][0] = 0.35897
  expected.mat[2][1] = 0.35897
  expected.mat[2][2] = 0.43590
  expected.mat[2][3] = 0.92308
  
  expected.mat[3][0] = -0.69231
  expected.mat[3][1] = -0.69231
  expected.mat[3][2] = -0.76923
  expected.mat[3][3] = -1.92308
  
  b = a.inverse(a)
  assert(expected == b)

def invertMatrix3():
  a = Matrix(4, 4) 
  expected = Matrix(4, 4)
  
  a.mat[0][0] = 9
  a.mat[0][1] = 3
  a.mat[0][2] = 0
  a.mat[0][3] = 9
  
  a.mat[1][0] = -5
  a.mat[1][1] = -2
  a.mat[1][2] = -6
  a.mat[1][3] = -3
  
  a.mat[2][0] = -4
  a.mat[2][1] = 9
  a.mat[2][2] = 6
  a.mat[2][3] = 4
  
  a.mat[3][0] = -7
  a.mat[3][1] = 6
  a.mat[3][2] = 6
  a.mat[3][3] = 2
  
  expected.mat[0][0] = -0.04074  
  expected.mat[0][1] = -0.07778
  expected.mat[0][2] =  0.14444
  expected.mat[0][3] = -0.22222
  
  expected.mat[1][0] = -0.07778
  expected.mat[1][1] =  0.03333
  expected.mat[1][2] =  0.36667
  expected.mat[1][3] = -0.33333
  
  expected.mat[2][0] = -0.02901
  expected.mat[2][1] = -0.14630
  expected.mat[2][2] = -0.10926
  expected.mat[2][3] =  0.12963
  
  expected.mat[3][0] =  0.17778
  expected.mat[3][1] =  0.06667
  expected.mat[3][2] = -0.26667
  expected.mat[3][3] =  0.33333
  
  b = a.inverse(a)
  assert(expected == b)

def invertMatrix4():
  a = Matrix(4, 4)
  b = Matrix(4, 4)
  
  a.mat[0][0] = 3
  a.mat[0][1] = -9
  a.mat[0][2] = 7
  a.mat[0][3] = 3
  
  a.mat[1][0] = 3
  a.mat[1][1] = -8
  a.mat[1][2] = 2
  a.mat[1][3] = -9
  
  a.mat[2][0] = -4
  a.mat[2][1] = 4
  a.mat[2][2] = 4
  a.mat[2][3] = 1
  
  a.mat[3][0] = -6
  a.mat[3][1] = 5
  a.mat[3][2] = -1
  a.mat[3][3] = 1
  
  b.mat[0][0] = 8
  b.mat[0][1] = 2
  b.mat[0][2] = 2
  b.mat[0][3] = 2
  
  b.mat[1][0] = 3
  b.mat[1][1] = -1
  b.mat[1][2] = 7
  b.mat[1][3] = 0
  
  b.mat[2][0] = 7
  b.mat[2][1] = 0
  b.mat[2][2] = 5	
  b.mat[2][3] = 4
  
  b.mat[3][0] = 6
  b.mat[3][1] = -2
  b.mat[3][2] = 0
  b.mat[3][3] = 5
  
  c = a*b
  assert( c*b.inverse(b) == a)