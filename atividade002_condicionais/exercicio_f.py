# Curso de Desenvolvimento de Sistemas
# Turma: 0152
# Autor: Danilo Rogerio Magalhães Amaro
# Data: 26/04/2024
# Programa em Python para Empresa "LeapYearCheck"
# (Para verificação de ano bissexto)

import os


os.system('cls')

# Entrada de dados
print('.'*70)
print('Verificação de ano bissexto')
print('.'*70)
print()
ano = int(input('Digite o ano: '))
resposta =''

# Condicionais
if ano % 4 == 0 and ( ano % 400 == 0 or ano % 100 != 0):
    resposta = 'é Bissexto'
else:
    resposta = 'não É Bissexto'

# Saida de dados
print('-'*70)
print(f'O ano {ano} {resposta} .')
print('-'*70)
print('Fim do Programa')



