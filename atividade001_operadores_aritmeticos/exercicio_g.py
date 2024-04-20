# imports
import os


# Limpando a tela
os.system('cls')

print('*'*70)
print(' Exercício "G" ')
print('*'*70)
print()

# Entrada de dados
metro = float(input('Digite valor em metros: '))
print()

# Processamento
centimetros = metro * 100
milimetros = metro * 1000

# Saida de dados
print('-'*70)
print(' RESULTADOS ')
print('-'*70)
print()
print(f'{metro} metros equivale a {centimetros} centimetros.')
print(f'{metro} metros equivale a {milimetros} milímetros')