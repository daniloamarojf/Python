# Faça um programa que leia o nome de uma pessoa e verifique 
# se a palavra 'Oliveira' está presente neste nome, mostrando True ou False.

import os


os.system('cls')

# entrada de dados
nome = str(input('Nome completo: '))
respota1 = True
reposta2 = False

print()
print(f'O nome "{nome}" contem "Oliveira"?')
if 'Oliveira' in nome:
    print(f'Resposta: {respota1} ')
else:
    print(f'Resposta: {reposta2}')