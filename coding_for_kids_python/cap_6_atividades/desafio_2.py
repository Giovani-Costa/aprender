import turtle

mandala = turtle.Turtle()
turtle.colormode(255)


def desenhar_circulo(
    mandala: turtle.Turtle, r: int, g: int, b: int, tamanho: int
) -> None:
    mandala.penup()
    mandala.goto(0, -tamanho)
    mandala.pendown()
    mandala.fillcolor(r, g, b)
    mandala.pencolor(r, g, b)
    mandala.begin_fill()
    mandala.circle(tamanho)
    mandala.end_fill()


desenhar_circulo(mandala, 10, 57, 128, 200)
desenhar_circulo(mandala, 14, 80, 179, 150)
desenhar_circulo(mandala, 81, 138, 224, 100)
desenhar_circulo(mandala, 54, 95, 156, 50)
mandala.ht()
input()
