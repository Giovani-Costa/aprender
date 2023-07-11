import turtle

turtle.colormode(255)
grossura = 7
tamanho = 75
arco_iris = turtle.Turtle()
arco_iris.pensize(grossura)
arco_iris.left(90)
cores = [
    (255, 0, 0),
    (255, 127, 0),
    (255, 255, 0),
    (0, 255, 0),
    (0, 0, 255),
    (75, 0, 130),
    (148, 0, 211),
]
for i in range(7):
    arco_iris.color(cores[i])
    arco_iris.circle(tamanho - grossura * i, 180)
    arco_iris.penup()
    arco_iris.left(90)
    arco_iris.forward(tamanho * 2 - 2 * grossura * i - grossura)
    arco_iris.left(90)
    arco_iris.pendown()
input()
