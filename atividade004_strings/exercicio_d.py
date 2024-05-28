# Faça um programa que leia uma frase e depois exiba na tela:
# • A frase em minúsculas, a frase em maiúsculas, 
# a quantidade de caracteres na frase e quantas letras tem a 2ª palavra na frase.


import os


os.system('cls')

# entrada de dados
frase = str(input('Frase: '))
frase_minusculas = frase.lower()
frase_maiusculas = frase.upper()
quantidade_caracteres = len(frase)
lista = frase.split(' ')
segunda_palavra = lista[1]
quantidade_segunda = len(segunda_palavra)

print('-'*70)
print(f'Com letras minusúlas: {frase_minusculas}')
print(f'Com letras maúsculas: {frase_maiusculas}')
print(f'Quantidade de caracteres: {quantidade_caracteres}')
# print(f'{lista}')
print(f'Quantidade de caracteres da 2ª palavra: {quantidade_segunda}')
print('-'*70)
