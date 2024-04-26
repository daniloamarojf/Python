# Curso de Desenvolveimneto de Sistemas
# Turma 0152
# Autor: Danilo Rogerio Magalhães Amaro
# Data: 24/04/2024
# Estudo de Condicionais Parte 1

import os


os.system('cls')

print('-'*70)
print('Estudo de Condicionais: Parte 1')
print('='*70)

# Entrada
numero = float(input('Digite um numero: '))
resposta = ''

# Condicional
if numero % 2 == 0:
    resposta = f'O número {numero} é par!'
else:
    resposta = f'O número {numero} é impar!'
    
# Saída
print('='*70)
print(resposta)
print('Fim do programa!\n') # \n saltar uma linha