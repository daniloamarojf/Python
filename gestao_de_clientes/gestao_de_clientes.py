import os


os.system('cls')

fisica = 'Pessoa Física'
juridica = 'Pessoa Juridica'

print('Tipo de cliente: [1] Pessoa física [2] Pessoa juridica')

cliente = int(input('Tipo cliente: '))
 
'''# for cliente in range(1, 2):
   
    if cliente == 0 or cliente >= 3:
        print('Digite 1 para pessoa física ou 2 para pessoa juridica')
        continue
    elif cliente == 1:
        cliente = fisica
    else:
        cliente = juridica
        break

print(f'Cliente: {cliente}') '''   

# Cadastro de Cliente Pessoa Fisica
nome = str(input('Nome:'))
cpf = int(input('CPF: '))
genero = str(input('Gênero: '))
cep = input('CEP: ')
rua = str(input('Rua: '))
numero_casa = str(input('Numero: '))
complemeto_casa = input('Complemento: ')
bairro = input('Bairro: ')
cidade = input('Cidade: ')
uf = input('UF: ')
data_nascimento = int(input('Data de nascimento: '))
email = str(input('E-mail:'))

# cadastro de pessoa juridica
razao_social = str(input('Razão Social: '))
Nome_fantasia = str(input('Nome Fantasia: '))
cnpj = int(input('CNPJ: '))
atividade = str(input('Atividadde econômica: '))
cep_juridica = input('CEP: ')
rua_juridica = str(input('Rua: '))
numero_juridica = str(input('Numero: '))
complemeto_juridica = input('Complemento: ')
