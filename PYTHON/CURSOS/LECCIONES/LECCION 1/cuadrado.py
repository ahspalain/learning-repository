import turtle

ventana = turtle.Screen()
ventana.bgcolor("white")
tortuga = turtle.Turtle()
tortuga.speed(1)

#dibujar un cuadrado

for movimiento in range(4):
    tortuga.forward(100)
    tortuga.right(90)

ventana.exitonclick()