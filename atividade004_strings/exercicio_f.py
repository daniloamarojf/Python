# Faça um programa que receba o nome completo de uma pessoa e, 
# posteriormente, imprima esse nome separadamente.


import os


os.system('cls')

# Entrada de dados
nome = str(input('Digite o nome completo: '))
lista = nome.split(' ')
nomes_separados = "\n".join(lista)

print()
print('-'*70)
print('Listando os nomes separadamente:')
print(f'{nomes_separados}')
print('-'*70)