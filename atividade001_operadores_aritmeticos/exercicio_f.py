# imports

import os


# Limpando a tela
os.system('cls')

print('*'*70)
print(' Exercício "F" ')
print('*'*70)
print()

# Entrada de dados
numero = float(input('Digite um numero: '))
print()

# Processamento
dobro = numero * 2
triplo = numero * 3

# Saída
print('-'*70)
print(' RESULTADO ')
print('-'*70)
print(f' O dobro do numero {numero} é: {dobro}')
print(f' O triplo de numero {numero} é: {triplo}')