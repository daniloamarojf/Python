import os


os.system('cls')

from gestao_clientes.pessoa_fisica.validacao import validar_cpf, validar_genero, validar_cep, validar_rua


# Cadastro de Cliente Pessoa Fisica
cpf_lista = []
genero_lista = []
cep_lista = []
rua_lista = []
    
def cadastro():  
    
    nome = str(input('Nome............................................: '))

    cpf = input('CPF.............................................: ')
    validar_cpf(cpf)
    cpf_lista.append(cpf)
    
    genero = str(input('Gênero M - Masculino | F - Feminino | O - Outros: ')).upper()
    validar_genero(genero)
    genero_lista.append(genero)
         
    cep = input('CEP.......................: ')
    validar_cep(cep)
    cep_lista.appende(cep)
         
    rua = str(input('Rua: ')).capitalize()
    validar_rua(rua)
    rua_lista.append(rua)
        
    numero = (input('Numero: '))

    complemeto = str(input('Complemento: '))
    bairro = input('Bairro: ')
    cidade = input('Cidade: ')
    uf = input('UF: ')
    data_nascimento = str(input('Data de nascimento: '))
    email = str(input('E-mail:'))

    return()

    # perguntas para perfil do cliente
    
cadastro()