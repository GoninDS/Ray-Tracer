import algorithms as alg

def menu_instructions():
  print("\n-------- Menu --------")
  print("0. Salir")
  print("1. Linea")
  print("2. Circulo")
  print("-------- Basados en angulos --------")
  print("3. Triangulo")
  print("4. Cuadrado")
  print("5. Hexagono")
  print("6. Octagono")
  print("7. Estrella")

def handle_cases(value):
  if value == 1:
    alg.bresenham_line()
  elif value == 2:
    alg.bresenham_circle()
  elif value == 3:
    alg.angle_algorithm(3, 120)
  elif value == 4:
    alg.angle_algorithm(4, 90)
  elif value == 5:
    alg.angle_algorithm(6, 60)
  elif value == 6:
    alg.angle_algorithm(8, 45)
  elif value == 7:
    alg.angle_algorithm(5, 144)

# Set for the loop
input_value = 1

while input_value > 0 and input_value < 8:
  menu_instructions()
  try:
    input_value = int(input())
    try:
      handle_cases(input_value)
    except:
      # Used to quick fix a bug
      handle_cases(input_value)
  except:
    print("\nPor favor inserte un valor valido")
    input_value = 1
  