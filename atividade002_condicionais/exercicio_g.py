# Curso de Desenvolvimento de Sistemas
# Turma: 0152
# Autor: Danilo Rogerio Magalhães Amaro
# Data: 26/04/2024
# Determinar se tês segmentos podem formar triângulo

import os


os.system('cls')

# Entrada de dados
print('.'*70)
print('Determinar se segmentos formam um triângulo')
print('.'*70)
print()

# Entrada de dados
a = int(input('1º Segmento: '))
b = int(input('2º Segmento: '))
c = int(input('3º Segmento: '))
resposta = ''
# Formula
# a < b + c
# b < a + c
# c < a + b

# Condicionais
if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
    resposta = 'Formam um triângulo'
else:
    resposta = 'NÂO formam um triangulo'
    
# saida de dados
print('-'*70)
print(f'Os segmentos fornecido {resposta}.')
print('-'*70)
print('Fim do Programa')