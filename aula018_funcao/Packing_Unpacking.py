import os


os.system('cls')

# Definindo uma função para empacotar
def empacotar(*lista_numeros):
    print(f'Empacotados: {lista_numeros}')
    for i in lista_numeros:
        print(f'Empacotados: {i}')
        
# invocando a função empacotar
empacotar = (1, 2, 3, 4, 5)

# Desempacotando lista
def desempacotar(a, b, c, d, e):
    print('Desempacotar:')
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
    print(f'd = {d}')
    print(f'e = {e}')
    
# Invocando a função empacotar
lista_numeros = [1, 2, 3, 4, 5]
desempacotar(*lista_numeros)

# Packing dicionário
def empacotar_dicionario(**dados_dicionario):
    print(f'Dados do dicionário> {dados_dicionario}')
    for k, v in dados_dicionario.items():
        print(f'Chave: {k}, Valor: {v}')
        
print('-'*70)
print('---Dicionário')
empacotar_dicionario(nome = 'Juquinha', idade = 70, peso = 70.5)

# Unpacking Dicionário
print('-'*70)
def desempacotar_dicionario(nome, idade, peso):
    print(f'Nome = {nome}')
    print(f'Idade = {idade}')
    print(f'Peso = {peso}')
    
dicionario = dict(nome = 'Maria', idade = 70, peso= 70.5)
desempacotar_dicionario(**dicionario)
print()