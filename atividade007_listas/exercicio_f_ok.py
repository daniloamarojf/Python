# Faça um programa que gere 10 números aleatórios. Após gerar esses números,
# crie duas listas novas com ordenação ascendente e descendente.

import os
import random


os.system('cls')

print('-'*70)
print('LISTA ASCEDENTE E DESCENDENTE')
print('-'*70)

lista = []
ascendente = []
descedente = []

for i in range(1, 10):
    
    numeros = random.randint(1, 500)
    lista.append(numeros)
    
print(f'Lista de números: {lista}')
lista.sort()
print()
print(f'Lista ascendente: {lista}')
lista.reverse()
print(f'Lista descendente: {lista}')