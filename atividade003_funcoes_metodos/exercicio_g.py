# Faça um programa que peça os valores de a, b e c de uma equação do 2º grau.
# Calcule as raízes da equação do 2º grau seguindo a fórmula:
# Δ = b² - 4ac, x = (-b ± raiz(Δ)) / (2a).

# importando biblioteca
import os
import math


os.system('cls')

#  Entrada de dados
a = int(input('Valor a: '))
b = int(input('Valor b: '))
c = int(input('Valor c: '))

# Processamento
b2 = math.pow(b, 2)
delta = b2 - (4 * a * c)
raiz_delta = math.sqrt(delta) # deve maior que 0    
x1 = ((-b + raiz_delta) / (2 * a))
x2 = ((-b - raiz_delta) / (2 * a))

# saída
print('-'* 70)
print(f'As raizes de  ')
print(f'X1 = {x1}')
print(f'X2 = {x2}')
print('-'*70)
print('--- Fim do Programa ---')