# Faça um programa que receba um número inteiro e mostre na tela:
#• A quantidade de unidades, a quantidade de dezenas, 
# a quantidade de centenas e a quantidade de milhares.


import os


os.system('cls')

# entrada de dados
numero = int(input('Numero: '))
unidade = numero % 10
dezena = (numero % 100) - unidade

# saida de dados
print(unidade)
print(dezena)
print(f'Número: {numero}')

