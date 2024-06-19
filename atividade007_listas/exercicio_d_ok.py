# Crie uma lista com 6 nomes, depois verifique se o nome ‘Pedro’ está nessa lista.

import os


os.system('cls')
lista = []

for i in range(1, 7):
    nome = input(f'{i}º Nome: ')
    lista.append(nome)
    
print(f'Nomes: {lista}')
print()
if 'pedro' in lista:
    print('A lista contem o nome "Pedro".')
else:
    print('A lista NÃO contem o nome "Pedro".')

print()
print('Fim do programa!')
