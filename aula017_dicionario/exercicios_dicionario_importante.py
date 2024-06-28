import os


os.system('cls')

# Inicialização do dicionário e lista
elementos = {} # dicionário
periodica = [] # lista

# entarda de dados
for c in range(2): # Considerando a entrada de 2 elementos
    print(f'Entrada de dados {c + 1}:')
    simbolo = str(input('Símbolo do elemento: '))
    nome = str(input('Nome do elemento: '))
    
    # Adiciona os dados ao dicionário
    elementos[simbolo] = simbolo
    elementos[nome] = nome
    
    # Usa append() com copy() para adicionar uma cópia do dicionário à lista 
    periodica.append(elementos.copy())
    
print()
print('-'*70)
print('Elementos da tabela periódica')
print(periodica)
print('-'*70)
print()

# for aninhado para percorrer a lista e o dicionário
print('Detalhes dos elementos')
for elementos in periodica: # Para cada elemento na lista
    for chave, valor in elementos.items(): # Para cada chave e valor de dicionário
        print(f'{chave.capitalize()}: {valor}') # Imprime a chave e o valor de maneira legível
    print('-'*70) # Linha separadora entre elementos
    