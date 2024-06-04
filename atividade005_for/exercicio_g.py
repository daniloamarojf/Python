# Faça um programa que calcule os números primos em um intervalo pré-determinado pelo usuário.

import os


os.system('cls')

inicio = int(input('Inicio: '))
final = int(input('Final: '))

for var_iteradora in range(inicio, final+1):
    contar = 0
    
    for var_iteradora1 in range(inicio, final+1):
        if var_iteradora % var_iteradora1 == 0:
            contar = contar + 1
            
    if contar == 2:
        print(f'{var_iteradora}', end=", ")