# Faça um programa para criar um dicionário com 5  cores. Depois, 
# imprima as chaves e os valores deste dicionário.

import os

os.system('cls')

print('-'*50)
print('DICIONÁRIO DE CORES')
print('-'*50)


cores = {}

for i in range(5):
    # Adicionando Chaves:valor ao dicionário
    chave = (f'Cor{i+1}')
    valor = (input(f'Digite a cor{i+1}: '))
    cores[chave] = valor

print()
print(f'Cores: {cores}')