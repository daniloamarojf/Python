import os


os.system('cls')

print('-'*70)
print('EXTRUTURA DE DADOS: DICIONÁRIO')
print('='*70)

compras = {}
pessoas = {}
cores = {}
elementos = dict()
numeros = dict()

# Atribuindo valores
compras['id'] = 1
compras['Item'] = 'caderno'
compras['valor'] = 10.80

pessoas['id'] = '0010'
pessoas['nomes'] = 'Sherlock Holmes'
pessoas['endereço'] = 'Baker Street'
pessoas['numero'] = '221B'
pessoas['cidade'] = 'Londres'
pessoas['pais'] = 'Inglaterra'

cores['red'] = 'vermelho'
cores['green'] = 'verde'
cores['blue'] = 'azul'

elementos['Pb'] = 'chumbo'
elementos['Au'] = 'Ouro'
elementos['N'] = 'Nitrogênio'

numeros[1] = 100
numeros[2] = 200
numeros[3] = 300

# Saída simples
print(f'Minhas compras: {compras}')
print(f'Detetives: {pessoas}')
print(f'Cor RGB: {cores}')
print(f'Tabela periódica: {elementos}')
print(f'Listagem de números: {numeros}')
print()
print('-'*100)