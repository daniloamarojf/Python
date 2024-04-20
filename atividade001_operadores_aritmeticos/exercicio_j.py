# imports
import os


# Limpando o sistema
os.system('cls')

# Entrada de dados
print('*'*70)
print(' Exercício "J" ')
print('*'*70)
print()
lado = float(input('Medida do lado do retângulo..: '))
altura = float(input('Medida da altura do retângulo: '))

# Processamento
lados = lado * 2
alturas = altura * 2
perimetro = lados + alturas

# Saida de dados
print('-'*70)
print(' RESULTADOS ')
print('-'*70)
print()
print(f'Retângulo com medidas: {lado} de lado e {altura} de altura')
print(f'seu perímetro é:   {perimetro}')