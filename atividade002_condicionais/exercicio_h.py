# Curso de Desenvolvimento de Sistemas
# Turma: 0152
# Autor: Danilo Rogerio Magalhães Amaro
# Data: 26/04/2024
# Programa em Python para Empresa "RootCalc"
# (Para calculo de raízes da equação)

import os


os.system('cls')

# Cabeçalho
print('.'*70)
print('Calculos de raizes da equação')
print('.'*70)
print()

# Declarações
a = 1
b = -6
c = 5
delta = ((b ** 2)-(4 * a * c)) 
delta_elevado = delta ** 0.5

# Condicionais
x = (-b + (delta ** 0.5)) / (2 * a)
x1 = (-b - (delta ** 0.5)) / (2 * a)


print('-'*70)
print(f'Resultado de x é: {x}')
print(f'Resultado de x1 é {x1}')
print('-'*70)
print('Fim do Programa')