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
    
# Solicita ao usuário para inserir o número que deseja contar na lista
numero_para_contar = int(input('Digite o número que deseja contar: '))

# Conta o númro de vezes que o numero fornecido aparece na lista
contagem = numeros.count(numero_para_contar)

if contagem > 0:
    print(f'O número {numero_para_contar} aparece {contagem} vezes na lista.')
else:
    print(f'O número {numero_para_contar} não aparece na lista.')
    
# Exibir a lista fornecida para referência
print(f'Lista fornecida: {numeros}')