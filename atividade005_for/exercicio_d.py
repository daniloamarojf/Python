# Faça um programa que imprima os números pares entre 0 e 100.

import os


os.system('cls')

print()
print('Números pares entre 0 e 100')
for var_interadora in range(2, 101, 2):
    print(f'{var_interadora}', end=" | ")