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
multiplicando = float(input('Entre com o multiplicando: '))
multiplicador = float(input('Entre com o multiplicador: '))

print()
print('---DIVISÃO')
print('-'*70)
dividendo = float(input('Entre com o dividendo: '))
divisor = float(input('Entre com o divisor: '))

print()
print('---RAIZ QUADRADA')
print('-'*70)
radicando_quadrado = float(input('Entre com o radicando: '))

print()
print('---RAIZ CUBICA')
print('-'*70)
radicando_cubico = float(input('Entre com o radicando: '))


# Processamento
soma = parcela_01 + parcela_02
diferenca = minuendo - subtraendo
produto = multiplicando * multiplicador
quociente = dividendo / divisor
raiz_quadrada = radicando_quadrado ** 1/2
raiz_cubica = radicando_cubico ** 1/3

# Saida
print('='*70)
print('RESULTADOS')
print('-'*70)
print(f'A soma de {parcela_01} + {parcela_02} é: {soma}')
print(f'A subtração de {minuendo} - {subtraendo} é: {diferenca}')
print(f'A multiplicaçao de {multiplicando} x {multiplicador} é: {produto}')
print(f'A divisão de {dividendo} ÷ {divisor} é: {quociente}')
print(f'A raiz quadrada de {radicando_quadrado} é: {raiz_quadrada}')
print(f'A raiz cubica de {radicando_cubico} é: {raiz_cubica}')
       
 # Seguindo os passos anteriores, desenvolva o restante
 # Acrescente a raiz quadrada e a raiz cubica   
  