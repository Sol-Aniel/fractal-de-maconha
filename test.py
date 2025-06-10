import turtle
import random

# Setup da janela
screen = turtle.Screen()
screen.bgcolor("#390d2d")
screen.tracer(0)

# Setup da tartaruga
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.speed(0)
t.color("#fe4b74")  # cor tipo "verde samambaia"

# Inicialização
x, y = 0, 0

def transform(p, x, y):
    if p == 1:
        return 0, 0.16 * y
    elif 2 <= p <= 86:
        return 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
    elif 87 <= p <= 93:
        return 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
    else:
        return -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44

# Escala para coordenadas da tela
def map_to_screen(x, y):
    return x * 60, y * 60 - 300  # ajuste para melhor visualização

# Loop de geração do fractal
for _ in range(99999):  # menos pontos para desempenho razoável
    p = random.randint(1, 100)
    x, y = transform(p, x, y)
    sx, sy = map_to_screen(x, y)
    t.goto(sx, sy)
    t.dot(2)

screen.update()
screen.mainloop()
