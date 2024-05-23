# Faça um programa que solicite separadamente o nome, o nome do meio e o sobrenome de uma pessoa.
# Em seguida, imprima o nome completo.

import os


os.system('cls')

# entrada de dados
nome = str(input('Nome: '))
segundo_nome = str(input('Segundo nome: '))
sobre_nome = str(input('Sobrenome: '))
lista = [nome, segundo_nome, sobre_nome]
nome_completo = " ".join(lista)

# saida de dados
print('-'*70)
print(f'Nome completo: {nome_completo}')
print('-'*70)
