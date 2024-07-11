import os

os.system('cls')

cpf_lista = []

while True:
    cpf = input('cpf: ')
    if not cpf.isdigit() or len(cpf) != 11:  
        print('CPF inválido!')
        continue

    cpf_lista.append(cpf)
    cep = input('cep: ')
    break
