# Faça um programa que receba as informações de base e expoente. Calcule a potência.
# Importando bibliotecas

import os
import math


print('-'*70)
print('Para calculo da potência, digite a base e o expoente')
print('-'*70)

 
base = int(input('Digite a base: '))
expoente = int(input('Digite e expoete: '))
potencia = math.pow(base, expoente)
print(f'A potência de {base} elevado a {expoente} é: {potencia}')
print('Fim do programa')