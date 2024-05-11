# Faça um programa que receba 2 valores, faça a divisão entre eles.
# Se a divisão não for inteira, o programa deverá arredondar o 
# resultado para cima e para baixo. Faça a validação para divisão por 0.

# imprtando biblioteca
import os
import math


# Limpando o terminal
os.system('cls')

# Entrada de dados
valor1 = float(input('Digite o 1º valor: '))
valor2 = float(input('Digite o 2º valor: '))


if valor2 == 0:
    print(f'Valor deve ser diferente de 0')
elif valor1 % valor2 != 0:
    print(f'Resultado não é numero interio')
else:
    print(f'Resultado da divisão é :{divisao}')
    
# Processamento
divisao = valor1 / valor2
arredondar_cima = math.ceil(divisao)
arredondar_baixo = math.floor(divisao)

print(f'Valor arredondado para cima é...: {arredondar_cima}.')
print(f'Valor arredondado para baixo é..: {arredondar_baixo}')