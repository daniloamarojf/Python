# Crie uma função que receba uma lista de números.
# Depois retorne duas listas com os números pares, os números ímpares, 
# a quantidade de números pares e a quantidade de números ímpares.

# 
import os


os.system('cls')

def pegar_par_impar(lista):
    pares = []
    impares = []
    print(f'Lista: {lista}')
    for i in lista:
        if (i % 2 == 0):
            pares.append(i)
        else:
            impares.append(i)
            
    print(f'Lista possui {len(pares)} números pares.')
    print(f'Lista pares: {pares}')
    print()
    print(f'Lista possui {len(impares)} números ímpares.')
    print(f'Lista ímpares: {impares}')
    
    return pares

lista = [1, 2, 3, 4, 5, 6]

pegar_par_impar(lista)