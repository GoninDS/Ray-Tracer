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
      pass
  elif value == 4:
    pass
  elif value == 5:
    pass
  elif value == 6:
    pass
  elif value == 7:
    pass

# Set for the loop
input_value = 1

while input_value > 0 and input_value < 8:
  menu_instructions()
  try:
    input_value = int(input())
    handle_cases(input_value)
  except:
    print("\nPor favor inserte un valor valido")
    input_value = 1
  