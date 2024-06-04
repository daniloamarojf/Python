# Evolua o programa anterior para um código que pergunte 
# ao usuário qual o intervalo que ele deseja ver  impresso.

import os


os.system('cls')


print()
inicio = (int(input('Número inical: ')))
final = (int(input('Numero final: ')))

for var_iteradora in range(inicio, final+1):
        print(f'{var_iteradora}', end=" | ")
    