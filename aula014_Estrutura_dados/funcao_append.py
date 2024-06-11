import os


os.system('cls')
# Inicializa uma lista fazia
lista_numeros = []

# Pede ao usuário para inserir 3 números
for i in range(3):
    numero = int(input('Digite um numero: '))
    
    # adiciona o número à lista
    lista_numeros.append(numero)
    
    # Verifica se o número inserido está na lista e
    # exibe uma mensagem correspondente
numero_verificar = int(input('Digite um numero: '))

if numero_verificar in lista_numeros:
    print(f'O número {numero_verificar} está na lista!')
else:
    print(f'O número {numero_verificar} não está na lista.')                 