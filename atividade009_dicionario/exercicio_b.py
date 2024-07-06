# Utilizando o exercício anterior,  adicione mais 2 elementos ao dicionário.

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
    
print(f'Dicionário: {elementos}')

elementos['mês'] = 'Janeiro'
elementos['ano'] = 2000

print(f'Novo dicionário: {elementos}')