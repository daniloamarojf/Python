# Faça um programa que receba 7 números inteiros. Depois quebre essa lista em:
# lista de pares e lista de ímpares. 

import os


os.system('cls')

print('-'*70)
print('LISTA DE NÚMEROS PARES E ÍMPARES')
print('-'*70)

lista = []
pares = []
impares = []

for i in range(1, 8):
    numero = int(input(f'{i}º Numero: '))
    lista.append(numero)
    
    if (numero % 2 == 0):
        pares.append(numero)
    else:
        impares.append(numero)
   
print(f'Lista: {lista}')
print()
print(f'Numeros pares: {pares}')
print(f'Números ímpares: {impares}')
print()
print('Fim do programa!')