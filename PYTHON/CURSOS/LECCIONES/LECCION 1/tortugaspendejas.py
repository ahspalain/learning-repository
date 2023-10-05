import turtle
import random

#crear ventana de enseñanza python
#width ancho
#height alto

ventana = turtle.Screen()
ventana.title("Carrera de Tortugas Esquizofrenicas")
ventana.bgcolor("skyblue")
ventana.setup(width=800, height=600)

caracol1 = turtle.Turtle()
caracol1.shape("turtle")
caracol1.color("red")
caracol1.penup()
caracol1.goto(-300,50)

caracol2 = turtle.Turtle()
caracol2.shape("turtle")
caracol2.color("black")
caracol2.penup()
caracol2.goto(-300,-50)

meta = 300

while caracol1.xcor() <300 and caracol2.xcor() <300:
    avance_caracol1 = random.randint(1,20)
    avance_caracol2 = random.randint(1,20)

    caracol1.forward(avance_caracol1)
    caracol2.forward(avance_caracol2)

    print(f'El caracol1 avanza {avance_caracol1}, para un total de {caracol1.xcor()}')
    print(f'El caracol1 avanza {avance_caracol2}, para un total de {caracol2.xcor()}')
    print("--------------------------------")

if caracol1.xcor() < caracol2.xcor():
    print("El caracol 2 es el vencedor.")
elif caracol1.xcor() > caracol2.xcor():
    print("El caracol 1 es el vencedor.")
else:
    print("Esto es un empate.")

ventana.exitonclick()