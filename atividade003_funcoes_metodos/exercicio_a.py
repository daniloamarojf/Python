# Faça um programa que receba um valor e mostre sua raiz quadrada.
# Para raízes que não são exatas, arredonde para cima ou para baixo.
# Faça a validação para números negativos, avisando ao usuário que 
# o resultado será um número complexo

# imprtando biblioteca
import os
import math


# Limpando o terminal
os.system('cls')

# Entrada de dados
valor = int(input('Digite um número: '))

# Processamento
raizQuadrada = math.sqrt(valor)
raiz_arredondada = math.floor(raizQuadrada)

# Saída
print('-'* 70)
print(f'A raiz quadrada do número {valor} é: {raiz_arredondada}')
print('-'*70)
print('--- Fim do Programa ---')

# faltando *****Faça a validação para números negativos, avisando ao usuário que 
# o resultado será um número complexo (cmath)