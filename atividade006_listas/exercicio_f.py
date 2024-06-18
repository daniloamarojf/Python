# Faça um programa que leia 5 nomes, depois imprima estes nomes com seus respectivos índices.

import os


os.system('cls')

print('-'*70)
print('Lista de nomes')
print('-'*70)

lista = []
# Entrada de dados
for i in range(1, 5):
    nome = input(f'{i}º Nome: ')
    lista.append(nome)

print('-'*70)
print('Lista de nomes e índices')
print('-'*70)

for indice, nome in enumerate(lista):
    print(f'indice: {indice} - Nome: {nome}')
    
