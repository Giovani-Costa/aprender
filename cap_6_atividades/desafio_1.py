import turtle


def desenhar_estrela(caneta: turtle.Turtle, x: int, y: int, tamanho: int) -> None:
    caneta.penup()
    caneta.goto(x, y)
    caneta.pendown()
    caneta.pencolor("yellow")
    caneta.pensize(5)
    for _ in range(5):
        caneta.right(144)
        caneta.forward(tamanho)


turtle.Screen().setup(500, 500)
turtle.Screen().bgcolor("darkblue")
caneta = turtle.Turtle()
desenhar_estrela(caneta, -20, 40, 90)
desenhar_estrela(caneta, 50, 70, 60)
desenhar_estrela(caneta, 140, 120, 50)
desenhar_estrela(caneta, -120, 150, 110)
caneta.penup()
caneta.goto(-250, -100)
caneta.pendown()
caneta.goto(250, -100)
tartaruga = turtle.Turtle()
tartaruga.color("green")
tartaruga.shape("turtle")
tartaruga.penup()
tartaruga.goto(0, -150)
tartaruga.left(90)
input()
