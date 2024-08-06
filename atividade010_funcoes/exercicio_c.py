# Crie uma função que verifica se uma aluno está cadastrado ou não em um dicionário.
# Se estiver cadastrado, imprima o nome desse aluno e o resto dos seus dados.
# O dicionário deverá conter nome, matrícula e a data de nascimento do aluno.

import os


os.system('cls')

cadastro = {}

def cadastrar_aluno(aluno):
    nome = input('Nome: ')
    matricula = input('Matricula: ')
    data_nascimento = input('Data nascimento: ')
    
    cadastro['nome'] = nome
    cadastro['matricula'] = matricula
    cadastro['data_nascimento'] = data_nascimento
    
    print(cadastro)
    
    
    return aluno
    
   
cadastrar_aluno(cadastro)


def verificar_aluno(nome):
    aluno = input('Qual nome quer verificar: ')
    if aluno in cadastro:
        print('certo')
    else:
        print('nao')
    return nome

verificar_aluno(aluno)
