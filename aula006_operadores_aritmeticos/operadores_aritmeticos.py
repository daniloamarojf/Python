# imports
import os

# Limpar terminal
os.system('cls')

print('-'*70)
print('OPERADORES ARITMETICOS')
print('='*70)

# entrada de dados
print('---SOMA')
print('-'*70)
parcela_01 = float(input('Entre com a 1ª parcela: '))
parcela_02 = float(input('Entre com a 2ª parcela: '))

print()
print('---subtração')
print('-'*70)
minuendo = float(input('Entre com o minuendo: '))
subtraendo = float(input('Entre com o subtraendo: '))

print()
print('---PRODUTO')
print('-'*70)
multiplicando = folat(input('Entre com o multiplicando: '))
multiplicador = float(input('Entre com o multiplicador'))

print()
print('---DIVISÃO')
print('-'*70)
dividendo = float(input('Entre com o dividendo: '))
divisor = float(input('Entre com o divisor: '))

# Processamento
soma = parcela_01 + parcela_02
diferenca = minuendo - subtraendo
produto = multiplicando * multiplicador
quociente = dividendo / divisor

# Saida
print('='*70)
print('RESULTADOS')
print('-'*70)
print(f'A soma de {parcela_01} + {parcela_02} é: {soma})
print(f'A subtração de {minuendo} - {subtraendo} é: {diferenca})
print(f'A multiplicaçao de {multiplicando} x {multiplicador} é: {produto})
 
 # Seguindo os passos anteriores, desenvolva o restante
print(f'A divisão de {dividendo} ÷ {divisor} é: {quociente})
 # Acrescente a raiz quadrada e a raiz cubica     