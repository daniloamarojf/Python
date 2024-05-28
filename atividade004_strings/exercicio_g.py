# Faça um programa que receba um número inteiro e mostre na tela:
#• A quantidade de unidades, a quantidade de dezenas, 
# a quantidade de centenas e a quantidade de milhares.


import os


os.system('cls')

# entrada de dados
numero = int(input('Numero: '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

# saida de dados

print()
print('-'*70)
print(f'Unidades: {unidade}')
print(f'Dezenas: {dezena}')
print(f'Centenas: {centena}')
print(f'Milhar: {milhar}')
print('-'*70)