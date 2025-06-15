import matplotlib.pyplot as plt 
from random import randint
from turtle import *
import numpy as np
import matplotlib.pyplot as plt

# criando os arrays de x e y para armazenar os valores
x = [0]
y = [0]

#loop para executar 50.000 vezes e a cada uma delas marcar um novo ponto
for i in range(500000): 
  
    p = randint(1, 100) #uso da função randit para escolher um número aleatório entre 1 e 100
    
      
    if p == 1: 
        x.append(0) #se o número for 1 o novo x se torna 0 e o y diminui 16% em seu valor anterior
        y.append(0.16*(y[i])) 
         
    if p >= 2 and p <= 86: 
        x.append(-0.85*(x[i]) - 0.04*(y[i])) 
        y.append(-0.04*(x[i]) + 0.85*(y[i])+1.6) #se o número for menor ou igual a 86 o novo x se torna 0 e o y diminui 16% em seu valor anterior
      
    if p >= 87 and p <= 93:  
        x.append(-0.2*(x[i]) + 0.26*(y[i])) 
        y.append(0.23*(x[i]) + 0.22*(y[i])+1.6) 
          
    if p >= 94 and p <= 100: 
        x.append(0.15*(x[i]) - 0.28*(y[i])) 
        y.append(0.26*(x[i]) + 0.24*(y[i])+0.44)

plt.scatter(x, y, s = 0.5, c ='#ec6363') 
plt.axis("off")
plt.show()