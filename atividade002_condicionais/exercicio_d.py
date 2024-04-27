# Curso de Desenvolvimento de Sistemas
# Turma: 0152
# Autor: Danilo Rogerio Magalhães Amaro
# Data: 25/04/2024
# Programa em Python para Empresa "SalaryBoost"
# (Para calculo de aumanento salarial)

import os


os.system('cls')

# Entrada de dados
print('.'*70)
print('Calculo de aumento salarial')
print('.'*70)
print()

#  Condicionais       (nao pode ser igual a 0 e nem negativo)
salario_atual = float(input('Valor do salario atual: '))
acrescimo = ''

if salario_atual > 1500:
    acrescimo = salario_atual * 0.05
elif salario_atual < 1000:
    acrescimo = salario_atual * 0.10
else:
    acrescimo = 0
    
novo_salario = salario_atual + acrescimo
    
    # saida de dados
print('-'*70)
print(f'O salário atual será acrescido de {acrescimo}.')
print(f'Sendo assim o novo salário será {novo_salario}')
print('-'*70)
print('Fim do Programa')