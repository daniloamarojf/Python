# Faça um programa que receba o nome completo de uma pessoa e, 
# posteriormente, imprima esse nome separadamente.


import os


os.system('cls')

# Entrada de dados
nome = str(input('Digite o nome completo: '))
lista = nome.split(' ')

print(f'{lista}')
for i in lista:
    print(i)