# Faça um programa que receba 2 valores, faça a divisão entre eles.
# Se a divisão não for inteira, o programa deverá arredondar o 
# resultado para cima e para baixo. Faça a validação para divisão por 0.

# imprtando biblioteca
import os
import math


# Limpando o terminal
os.system('cls')

# Entrada de dados
valor1 = int(input('Digite o 1º valor: '))
valor2 = int(input('Digite o 2º valor: '))

# Processamento
divisao = valor1 / valor2

if divisao % 2 == 0:
    divisão_interio = divisao
