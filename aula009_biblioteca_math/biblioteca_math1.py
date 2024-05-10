import os
import math


os.system('cls')

print('-'*50)
print('ESTUDO DA BIBLIOTECA MATEMATICA MATH')
print('='*50)
print()

# Entrada de dados
numero_decimal = float(input('Entre com um numero deciaml: '))

# Processamento
arredondar_para_cima = math.ceil(numero_decimal)
arredondar_para_baixo = math.floor(numero_decimal) 

# Saida
print(f'O numero {numero_decimal} arredondado para cima é {arredondar_para_cima}')
print(f'O numero {numero_decimal} arredondado para baixo é {arredondar_para_baixo}')
print('-'*50)
