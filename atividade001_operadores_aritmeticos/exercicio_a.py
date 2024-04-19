#import

import os


os.system('cls')

print('*'*70)
print(' Exercício "A"')
print('*'*70)

# Entrada de dados
primeiro_valor = (float(input('Entre com o 1º valor: ')))
segundo_valor = (float(input('Entre com o 2º valor: ')))
terceiro_valor = (float(input('Entre com o 3º valor: ')))

# Processamento
soma = primeiro_valor + segundo_valor + terceiro_valor
produto = primeiro_valor * segundo_valor * terceiro_valor

# saídas
print('-'*70)
print(' RESULTADOS ')
print('-'*70)
print()
print(f'A soma dos valores é: {soma}')
print(f'A multiplicação dos valoes é: {produto}')