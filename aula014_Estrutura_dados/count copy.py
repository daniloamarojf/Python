import os


os.system('cls')

# Solicita ao usuário para inserir números separados por espaço
entrada = input('Digite números separados por espaços: ')

# Divide a strig de entrada em uma lista de string
numeros_str = entrada.split()

# converte a lista de string  em uma lista de inteiros
numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str)) 
    
# Solicita ao usuário para inserir um número que deseja encontrar na lista
busca_numero = int(input('Digite o número que deseja encontrar: ')) 

# tenta encontrar o indice do número fornecido
if busca_numero in numeros:
    indice = numeros.index(busca_numero)
    print(f'O número {busca_numero} está no indice {indice}')
else:
    print(f'O número {busca_numero} não foi encontrado na lista.')
    
# Exibe a lsita para referência
print(f'Lista fornecida: {numeros}')