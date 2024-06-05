# Crie um programa que realiza a contagem de 1 até 100, usando apenas de números ímpares, 
# ao final do processo exiba na tela quantos números ímpares foram encontrados nesse intervalo, 
# assim como a soma dos mesmos.

import os


os.system('cls')

contador = 0
soma = 0

for var_iteradora in range(1, 100, 2):
   
    contador = contador + 1
    soma += var_iteradora
    
print()
print(f'O intervalo [1 a 100] possui {contador} números impar.')
print(f'A soma dos números impares entre 1 e 100 é {soma}')
    
    
    