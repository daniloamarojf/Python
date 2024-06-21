import os


os.system('cls')

# inicializa a lista vazia
lista_numeros = [10, 20]

# Solicita ao usuario que insira números separados por espaços
entrada = input('Digite números separados por espaços: ')

# Divide a string de entrada em uma lista de strings
numeros = entrada.split()

# Cria uma lista para armazenas números pares
pares = []

# itera sobre os números inseridos
for numero in numeros:
    # Converte a string em inteiros
    numero_aux = int(numero)
    # verifica se o número é par
    if numero_aux % 2 == 0:
        # Adiciona o número par a lista de pares
        pares.append(numero_aux)
        
# usa o extend() para adicionar todos os números pares à lista principal
lista_numeros.extend(pares)

# Exibe  a lista resultante
print(f'Números pares adicionados à lista: {lista_numeros}')
                