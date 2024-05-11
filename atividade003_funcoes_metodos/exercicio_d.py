# Faça um programa que receba um ângulo qualquer. 
# Em seguida, calcule o seno, cosseno e tangente do ângulo, 
# limitando a saída a 2 casas decimais.

# imprtando biblioteca
import os
import math


# Limpando o terminal
os.system('cls')

# Declaração
angulo = 50

# Processamento (seno, cosseno e tangente)
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

# saída
print('-'* 70)
print(f'Para o angulo {angulo}')
print(f'Seno: {seno:.2f} | Cosseno: {cosseno:.2f} | Tangente: {tangente:.2f}')
print('-'*70)
print('--- Fim do Programa ---')
 