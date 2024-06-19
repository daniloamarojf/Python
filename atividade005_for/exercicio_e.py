# Faça um programa que some a quantidade de números pares encontrados no intervalo entre 0 e 100.

import os


os.system('cls')

soma = 0

print('Soma dos números pares entre 0 e 100')
for var_iteradora in range(0, 101):
    
    if var_iteradora % 2 == 0:
        soma += 1
        print(f'{var_iteradora}', end=" | ")
    
    
print(f'A quantidade dos números é: {soma}')
    