# Utilizando o exercício anterior, coloque todas as listas em ordem crescente de valor

import os
import random


os.system('cls')

print('-'*70)
print('Números aleatório')
print('-'*70)

lista = []
intervalo1 = []
intervalo2 = []
intervalo3 = []
intervalo4 = []
intervalo5 = []
#lista_ordem = []


for i in range(1, 50):
    
    numeros = random.randint(1, 500)
    lista.append(numeros)
    #lista_ordem = lista.sort()

intervalo1 = lista[:10] 
intervalo2 = lista[11:20]   
intervalo3 = lista[21:30]
intervalo4 = lista[31:40]
intervalo5 = lista[41:50]
print(f'Lista de numeros aleatório: {lista}')
print()
print(f'Primeiro intervalo: {intervalo1}')
print(f'Segundo intervalo: {intervalo2}')
print(f'Terceiro intervalo: {intervalo3}')
print(f'Quarto intervalo: {intervalo4}')
print(f'Quinto intervalo: {intervalo5}')
lista.sort()
print()
print(f'Lista em ordem crescente: {lista}')
print()
print('Fim do programa!')