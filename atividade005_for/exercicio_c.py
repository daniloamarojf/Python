# Faça um programa que imprima os números no intervalo entre 1 e 10 em ordem inversa.

import os


os.system('cls')

print('Numeros de 1 a 10 invertido:')
for var_iteradora in range(10, 0, -1):
    print(f'{var_iteradora}', end=" | ")
        
