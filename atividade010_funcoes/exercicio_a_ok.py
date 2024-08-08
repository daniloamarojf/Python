# Crie uma função que receba uma lista de números.
# Depois retorne duas listas com os números pares, os números ímpares, 
# a quantidade de números pares e a quantidade de números ímpares.

# Importando biblioteca 
import os


os.system('cls')

# Definindo função pegar numeros pares e ímpares
def pegar_par_impar(lista):
    pares = [] # Criando lista vazia
    impares = [] # Criando lista vazia
    print(f'Lista: {lista}')
    
    # Verrendo a lista 
    for i in lista:
        if (i % 2 == 0):
            pares.append(i) # Adicionando números pares à lista
        else:
            impares.append(i) # Adicionando números impares à lista
    
    # Saída de dados        
    print(f'Lista possui {len(pares)} números pares.')
    print(f'Lista pares: {pares}')
    print()
    print(f'Lista possui {len(impares)} números ímpares.')
    print(f'Lista ímpares: {impares}')
    
    return pares

# Declarando uma lista
lista = [1, 2, 3, 4, 5, 6]

# Chamando a funçao 
pegar_par_impar(lista)