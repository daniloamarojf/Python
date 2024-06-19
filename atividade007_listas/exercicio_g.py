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

for i in range(1, 60):
    
    numeros = random.randint(1, 500)
    lista.append(numeros)
    
    # mostrar os numeros um após o outro de acordo com os indices