# Faça um programa onde o usuário tenta adivinhar o 
# número que o computador está ‘pensando’.

# imprtando biblioteca
import os
import random


# Limpando o terminal
os.system('cls')

# Entrada de dados
print(f'Tente descobrir o número que o computador irá gerar')
numero = int(input('Digite um número de 1 a 100: '))
numero_aleatorio = random.randint(1, 100)

if numero > 100:
    print('Numero deve ser menor que 100')
else:
    print(f'O número gerado é : {numero_aleatorio} ')
    if numero == numero_aleatorio:
        print(f'Você acertou.')
    else:
        print(f'Você errou.')
print('--- Fim do Programa ---')

