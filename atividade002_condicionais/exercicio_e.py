# Curso de Desenvolvimento de Sistemas
# Turma: 0152
# Autor: Danilo Rogerio Magalhães Amaro
# Data: 26/04/2024
# Programa em Python para Empresa "TravelCalc"
# (Para calcular preço de passagem de ônibus)

import os


os.system('cls')

# Entrada de dados
print('.'*70)
print('Calculo de preço de passagem de ônibus')
print('.'*70)
print()

# Entrada de dados
distancia = int(input('Qual a distância do percurso: '))
custo1 = 0.70
custo2 = 0.40
preco = ''

# Condicionais
if distancia <= 200:
    preco = distancia * custo1
else:
    preco = distancia * custo2
    
# saida de dados
print('-'*70)
print(f'O valor da passagem de ônibus será {preco}.')
print('-'*70)
print('Fim do Programa')
