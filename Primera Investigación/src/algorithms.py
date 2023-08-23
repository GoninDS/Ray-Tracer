import turtle

# ----------------- Algoritmo de linea -----------------
# Generado por medio de ChatGPT y editado posteriormente
def bresenham_line():
  x0 = int(input("Inserte la coordenada x para el primer punto: "))
  y0 = int(input("Inserte la coordenada y para el primer punto: "))
  x1 = int(input("Inserte la coordenada x para el segundo punto: "))
  y1 = int(input("Inserte la coordenada y para el primer punto: "))

  dx = x1 - x0
  dy = y1 - y0
  x = x0
  y = y0
  p = 2 * dy - dx
  
  while x < x1:
      turtle.penup()
      turtle.goto(x, y)
      turtle.pendown()
      turtle.dot(5, "red")
      
      if p >= 0:
          y += 1
          p += 2 * dy - 2 * dx
      else:
          p += 2 * dy
      x += 1
  turtle.done()

# ----------------- Algoritmo de circulo -----------------
# Generado por medio de ChatGPT y editado posteriormente
def draw_circle(xc, yc, x, y):
	turtle.penup()
	turtle.goto(xc + x, yc + y)
	turtle.pendown()
	turtle.dot(5, "red")
	turtle.penup()
	turtle.goto(xc - x, yc + y)
	turtle.pendown()
	turtle.dot(5, "red")
	turtle.penup()
	turtle.goto(xc + x, yc - y)
	turtle.pendown()
	turtle.dot(5, "red")
	turtle.penup()
	turtle.goto(xc - x, yc - y)
	turtle.pendown()
	turtle.dot(5, "red")
	turtle.penup()
	turtle.goto(xc + y, yc + x)
	turtle.pendown()
	turtle.dot(5, "red")
	turtle.penup()
	turtle.goto(xc - y, yc + x)
	turtle.pendown()
	turtle.dot(5, "red")
	turtle.penup()
	turtle.goto(xc + y, yc - x)
	turtle.pendown()
	turtle.dot(5, "red")
	turtle.penup()
	turtle.goto(xc - y, yc - x)
	turtle.pendown()
	turtle.dot(5, "red")

def bresenham_circle():
	r = int(input("Inserte el radio: "))
	xc = 0
	yc = 0
	x = 0
	y = r
	d = 3 - 2 * r
	draw_circle(xc, yc, x, y)
	while y >= x:
		x += 1
		if d > 0:
			y -= 1
			d = d + 4 * (x - y) + 10
		else:
			d = d + 4 * x + 6
		draw_circle(xc, yc, x, y)
		
# ----------------- Algoritmo en base de ángulos -----------------
# Tomado y modificado de GeeksforGeeks
def angle_algorithm(sides, angle):
  for i in range(sides):
    turtle.forward(100)
    turtle.right(angle)
  turtle.done()