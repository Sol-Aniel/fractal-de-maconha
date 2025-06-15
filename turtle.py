import turtle
import random

# Setup da janela
screen = turtle.Screen() #função da tela
screen.bgcolor("#390d2d") #cor de fundo
screen.tracer(0) #taxa de atualização da animação do turtle

# Setup da tartaruga
t = turtle.Turtle() 
t.hideturtle() #esconder a tartaruga
t.penup() #permitir a tartaruga se teletransportar pelos eixos sem rastros
t.speed(0) #velocidade max
t.color("#fe4b74")  # cor da samambaia

# Inicialização
x, y = 0, 0

def calcBarnley(p, x, y): #lógica de barnley, levando o número da probabilidade e das coordenadas
    if p == 1: #caule
        return 0, 0.16 * y
    elif 2 <= p <= 86: #folhas menores
        return 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
    elif 87 <= p <= 93: #folha grande da direita
        return 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
    else: #folha grande da esquerda
        return -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44
    
#outras versões:
def calcBarnley2(p, x, y): 
    if p <= 2:  
        a, b, c, d, e, f = 0, 0, 0, 0.25, 0, -0.4
    elif p <= 86:  
        a, b, c, d, e, f = 0.95, 0.005, -0.005, 0.93, -0.002, 0.5
    elif p <= 93:  
        a, b, c, d, e, f = 0.035, -0.2, 0.16, 0.04, -0.09, 0.02
    else:  
        a, b, c, d, e, f = -0.04, 0.2, 0.16, 0.04, 0.083, 0.12

    x_new = a * x + b * y + e
    y_new = c * x + d * y + f
    return x_new, y_new

# Escala para coordenadas da tela
def ampliarImagem(x, y):
    return x * 60, y * 60 - 300  # ajuste para melhor visualização

def ampliarImagem2(x, y):
    return x * 120, y * 120 - 500  

# Loop de geração do fractal
for _ in range(99999): 
    p = random.randint(1, 100) #fator aleatório
    x, y = calcBarnley2(p, x, y) #usando a segunda versão
    sx, sy = ampliarImagem2(x, y)
    t.goto(sx, sy)
    t.dot(2)

screen.update()
screen.mainloop()
