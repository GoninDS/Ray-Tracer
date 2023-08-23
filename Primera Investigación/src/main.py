
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

# Set for the loop
input_value = 1

while input_value > 0 and input_value < 8:
  menu_instructions()
  try:
    input_value = int(input())
    
  except:
    print("\nPor favor inserte un valor valido")
    input_value = 1
  