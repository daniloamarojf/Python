# imports
import os


# Limpando a tela
os.system('cls')

print('*'*70)
print(' Exercício "I" ')
print('*'*70)
print()

# Entrada de dados
valor_reais = float(input('Digite um valor em reais: R$ '))
dolar = float(input('Digite o valor atual do dolar: US$ '))

# Processamento
dolares_total = valor_reais / dolar

# Saidas
print('-'*70)
print(' RESULTADO ')
print('-'*70)
print()
print(f'Com {valor_reais} compramos {dolares_total:.2f} dólares.')