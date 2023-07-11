import turtle

from random import randint


def criar_tartaruga(posicao: int, cor: str) -> turtle.Turtle:
    tartaruga = turtle.Turtle()
    tartaruga.penup()
    tartaruga.shape("turtle")
    tartaruga.color(cor)
    tartaruga.goto(-300, posicao)
    tartaruga.pendown()
    return tartaruga


tartaruga_1 = criar_tartaruga(100, "red")
tartaruga_2 = criar_tartaruga(50, "orange")
tartaruga_3 = criar_tartaruga(0, "blue")
tartaruga_4 = criar_tartaruga(-50, "green")
tartaruga_5 = criar_tartaruga(-100, "yellow")
for _ in range(10):
    tartaruga_1.forward(randint(1, 100))
    tartaruga_2.forward(randint(1, 100))
    tartaruga_3.forward(randint(1, 100))
    tartaruga_4.forward(randint(1, 100))
    tartaruga_5.forward(randint(1, 100))
input()
