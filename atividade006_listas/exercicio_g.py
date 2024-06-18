# Ler uma lista com 10 números, depois apresente o maior e o menor número da lista

import os


os.system('cls')

print('-'*70)
print('Lista de números (maior e menor)')
print('-'*70)

lista = []
maior = 0
menor = 0

# Entrada de dados
for i in range(10):
    numero = input(f'{i}º Numero: ')
    lista.append(numero)
    
    if numero 
