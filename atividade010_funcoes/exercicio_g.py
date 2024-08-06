# Crie um programa que peça ao usuário 2 números maiores que 0 e menores que 11. 
# Depois mostre um menu com as seguintes operações:
# 1. Soma: 2. Subtração : 3. Produto : 4. Divisão : 4. Divisão inteira : 6. Resto da divisão.
# O usuário deverá escolher um número maior ou  igual a 1 e menor ou igual a 6. 
# Em seguida, você criará funções que retornem os resultados das operações,
# imprimindo os resultados na tela.

import os


os.system('cls')

print('-'*50)
print('Resultado de Operações Matemática')
print('-'*50)

for num in range(2):

    numero = (input('Digite um número de entre 0 e 11: '))
    

    if (not(numero.isnumeric())):
        print(f'{numero} Invalido!')
        print()
    else:
        numero = int(numero)
        if (numero >= 0 and numero <= 11):
            print('numero valido')
        else:
            print('Número ivalido!')
            
# while:
    