# Crie um programa que peça ao usuário 2 números maiores que 0 e menores que 11. 
# Depois mostre um menu com as seguintes operações:
# 1. Soma: 2. Subtração : 3. Produto : 4. Divisão : 4. Divisão inteira : 6. Resto da divisão.
# O usuário deverá escolher um número maior ou  igual a 1 e menor ou igual a 6. 
# Em seguida, você criará funções que retornem os resultados das operações,
# imprimindo os resultados na tela.

# Importanto bilbioteca
import os


os.system('cls')

# Criando função menu
def menu():
    print('Escolha a opção:')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Produto')
    print('4 - Divisão')
    print('5 - Divisão Inteira')
    print('6 - Resto da Divisão')
    
    return()

# Funções para calculo matemático
def soma(numero1, numero2):
    soma = numero1 + numero2
    print(f'A soma é : {soma}')
    return soma

def subtração(numero1, numero2):
    subtração = numero1 - numero2
    print(f'A subtração é : {subtração}')

    return subtração

def produto(numero1, numero2):
    produto = numero1 * numero2
    print(f'O produto é : {produto}')
    return produto

def divisao(numero1, numero2):
    divisao = numero1 / numero2
    print(f'A divisão é : {divisao}')
    return divisao

def divisao_intera(numero1, numero2):
    divisao_intera = numero1 // numero2
    print(f'A divisão inteira é : {divisao_intera}')
    return divisao_intera

def resto_divisao(numero1, numero2):
    resto_divisao = numero1 % numero2
    print(f'O resto da divisão é : {resto_divisao}')
    return resto_divisao

print('-'*50)
print('Resultado de Operações Matemática')
print('-'*50)

numero1 = int(input('Digite um número (> 0 e < 11): '))
numero2 = int(input('Digite um número (> 0 e < 11): '))

# Saída de dados 
soma(numero1, numero2)
subtração(numero1, numero2)
produto(numero1, numero2)
divisao(numero1, numero2)
divisao_intera(numero1, numero2)
resto_divisao(numero1, numero2)

