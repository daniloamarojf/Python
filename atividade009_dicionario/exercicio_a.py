# Faça um programa para criar um dicionário com 4 elementos.

import os


os.system('cls')

print('-'*50)
print('DICIONÁRIO COM 4 ELEMENTOS')
print('-'*50)

elementos = {}

for i in range(4):
    chave = input('Digite a chave: ')
    valor = input('Digite o valor: ')
    elementos[chave] = valor
    
print(f'{elementos}')
