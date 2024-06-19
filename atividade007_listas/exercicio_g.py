# Faça um programa que sorteia os números da Mega Sena e da Lotofácil


import os
import random


os.system('cls')

print('-'*70)
print('SORTEANDO NÚMEROS')
print('-'*70)

lista = []

print('-'*50)
print('MEGA SENA')
print('-'*50)

for i in range(1, 7):          
    
    numeros = random.randint(1, 60)
    lista.append(numeros)
    
    print(f'{i}º número sorteado: {numeros}')

print('-'*50)
print('LOTO FÁCIL')
print('-'*50)

for i in range(1, 15):
    
    numeros = random.randint(1, 25)     # FUNÇÃO ESTA REPETINDO NUMERO
    lista.append(numeros)
    
    print(f'{i}º número sorteado: {numeros}')
  