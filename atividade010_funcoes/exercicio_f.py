# Crie uma função que receba 2 listas: 
#- lista 1: nome, peso, idade
#- lista 2: John, 40, 1.8
#- Sua função deverá criar um dicionário contendo chave e valor utilizando 
# como base essas duas listas. Depois, seu programa deverá imprimir esse 
# dicionário utilizando uma estrutura de repetição for.

import os


os.system('cls')

print('-'*50)
print('Dicionários')
print('50'*50)

def criar_dicionario(chave, valor):
    dicionario = {}
    dicionario = zip(chave, valor)
    return(dicionario)
            
lista1 = ['nome', 'peso', 'idade']
lista2 = ['jhon', 40, 1.80]

