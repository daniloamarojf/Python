# Faça um programa que leia o nome de um aluno e 
# mostre quantas vezes a letra 'o' aparece
# e em que posição ela aparece pela primeira e última vez.

import os


os.system('cls')

# Entrada de dados
aluno = str(input('Digite do aluno: '))
letra = 'o'
quantidade_o = aluno.count(letra) 
primeiro_o = aluno.find(letra)+1
ultimo_o = aluno.rfind(letra)+1

print()
print(f'Quantidadde de o = {quantidade_o}')
print(f'O primeiro "o" aparece na {primeiro_o} posição.')
print(f'O último "o" aparece na {ultimo_o} posição.')