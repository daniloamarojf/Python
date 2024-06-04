# Faça um programa que imprima os números primos entre 0 e 100.
import os


os.system('cls')

for var_iteradora in range(0, 101):
    contar = 0
    
    for var_iteradora1 in range(1, 101):
        if var_iteradora % var_iteradora1 == 0:
            contar = contar + 1
            
    if contar == 2:
        print(f'{var_iteradora}', end=", ")