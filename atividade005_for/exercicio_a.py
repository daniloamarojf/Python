# Faça um programa que imprima os números no intervalo entre 1 e 100. 
# Os números devem ser apresentados na horizontal.

import os


os.system('cls')
print('Numero de 1 a 100:')

for var_iteradora in range(1, 101):
    print(f'{var_iteradora}', end=" | ")