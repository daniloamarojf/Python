# Faça um programa que receba o nome 'João da Silva' e, 
# em seguida, substitua 'Silva' por 'Oliveira'.


import os


os.system('cls')

# declaração
nome = 'João da Silva'
novo_nome = nome.replace('Silva', 'Oliveira')

# saida
print(f'Nome: {nome}')
print(f'Novo nome: {novo_nome}')