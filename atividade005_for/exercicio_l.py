# Faça um programa que verifique se o usuário e senha estão inseridos
# em um banco de dados (fake). O usuário só terá acesso se
# digitar os dados corretos e, assim, sair do laço.
import os


os.system('cls')

usuario1 = 'danilo'
senha1 = 1234

while (True):
    nome = str(input('Nome: '))
    senha = int(input('Senha: '))
    print()
    if (nome == usuario1 and senha == senha1):
        print('Usuário e senha estão CORRETOS')
        break
    else:
        print('Dados INCORRETOS. Continue...')
        print()
