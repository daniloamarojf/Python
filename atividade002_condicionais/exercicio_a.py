# Curso de Desenvolvimento de Sistemas
# Turma: 0152
# Autor: Danilo Rogerio Magalhães Amaro
# Data: 25/04/2024
# Programa em Python para Empresa "TechSolutions"
# (Para testar se o numero é inteiro)

import os


os.system('cls')

# Entrada de dados
print('.'*70)
print('Determinando se o número é par ou ímpar')
print('.'*70)
print()
numero = int(input('Digite um numero interio: '))
resposta =''
print()

# Condicionais
if numero % 2 == 0:
    resposta = 'PAR'
else:
    resposta = 'ÍMPAR'
    
    # Saída
print('-'*70)
print(f'O número {numero} é {resposta}')
print('-'*70)
print('Fim do Programa')