# Crie uma lista com 5 números inteiros. Depois imprima a soma desses valores.

import os


os.system('cls')

soma = 0
numero = 0

# entrada de dados
for c in range(1, 6):
    numero = input(f'{c}º Número: ')
    
    if (not (numero.isnumeric())):
        print('Número inválido!')
        print()
    else:
        numero = int
        
    soma += numero    
        
print(f'A soma dos números é {soma}')





        
        
    