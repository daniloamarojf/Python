# imports

import os
import datetime


# Limpando a tela
os.system('cls')

print('*'*70)
print(' Exercício "B" ')
print('*'*70)

# Entrada de dados
ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = datetime.datetime.now().year
print()

# Processamento
idade = ano_atual - ano_nascimento

# Saída
print('-'*70)
print(' RESULTADO ')
print('-'*70)
print()
print(f'Você possui {idade} anos.')