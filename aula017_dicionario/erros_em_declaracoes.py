import os


os.system('cls')

print('-'*70)
print('EXTRUTURA DE DADOS: DICIONÁRIO') # dict => {}
print('='*70)

# indices iguais: só irá exibir um item
dicionario1 = {'nome': 'Jhon', 'nome': 'Jane'}

# Posso ter uma tupla como índice e uma lista com valor
dicionario2 = {(1, 2): [1, 2]}

# Mas não posso ter uma lista com ídice e uma tupla como valor
dicionario3 = {[1, 2]: (1, 2)}

# Saída 
print('-'*80)
print(dicionario1)
print(dicionario2)

print()