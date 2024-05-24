# Faça um programa que receba o nome completo de uma 
# pessoa e, em seguida, mostre o primeiro e o último nome.

import os


os.system('cls')

# Entrada de dados
nome = str(input('Digite o nome completo: '))
lista = nome.split(' ')
primeiro_nome = lista[0]
ultimo_nome = lista[-1]

print()
print(f'Primeiro nome: {primeiro_nome}')
print(f'Último nome: {ultimo_nome}')