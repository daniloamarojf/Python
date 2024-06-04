# Faça um programa que imprima os valores no intervalo definidos pelo usuário. 
# Defina 3 números que deverão ser ignorados, ou seja, que não serão impressos na tela.

import os


os.system('cls')

inicio = int(input('Número inicial: '))
final = int(input('Número final: '))

for var_iteradora in range(inicio, final+1):
    if var_iteradora == 2:
        continue
    if var_iteradora == 5:
        continue
    if var_iteradora == 7:
        continue
    print(f'{var_iteradora}', end=", ")
        