# Faça um programa para sortear um número de 1 a 20.
import os

import random

 
os.system('cls')

print('-'*70)
print('Sorteio de numero aleatorio de 1 a 20')
print('-'*70)
numero_aleatorio = random.randint(1, 20)
print(f'O número sorteado é: {numero_aleatorio}')
print('Fim do programa.')