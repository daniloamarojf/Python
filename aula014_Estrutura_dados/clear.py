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
    
# Solicitao usuário para decidir se deseja limpar a lista
escolha = input('Deseja limpar a lista? (s/n): ').strip().lower()

# Verifica a escolha do usuário e limpa a lista se a resposta for 's'
if escolha == 's':
    numeros.clear()
    print(f'Lista limpa: {numeros}')
else:
    print('A lista não foi limpa.')
    
# Exibe a lista fornecida para referência
print(f'Lista fornecida:{numeros}')