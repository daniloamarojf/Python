# Crie uma função que cadastre o nome de um aluno, a matrícula e a data de nascimento. 
# Depois imprima os resultados cadastrados utilizando uma estrutura de repetição for.

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
    
    print('Cadastro de Alunos:')
    print()
    for chave, valor in cadastro.items():
        print(f'{chave}: {valor}')
    return aluno
    
   
cadastrar_aluno(cadastro)
        

       
