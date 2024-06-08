import os


os.system('cls')

print('Tipo de cliente: [1] Pessoa física [2] Pessoa juridica')
print()

while (True):
    cliente = int(input('Tipo cliente....................................: '))
    
    if cliente == 1 or cliente == 2:
        if cliente == 1:
            cliente = "Pessoa Fisica"
        else:
            cliente = "Pessoa Juridica"
        break 
    else:
        print('Digite 1 para pessoa física ou 2 para pessoa juridica')
        
print(f'Cliente.........................................: {cliente}')


# Cadastro de Cliente Pessoa Fisica

nome = str(input('Nome............................................: '))
cpf = int(input('CPF.............................................: '))
while (True):
    genero = str(input('Gênero M - Masculino | F - Feminino | O - Outros: ')).upper()
    
    if genero == 'M':
        genero = 'Masculino'
        print(f'Genero: {genero}')
        break
    elif genero == 'F':
        genero = 'Feminino'
        print(f'Genero: {genero}')
        break
    elif genero == 'O':
        genero = 'Outros'
        print(f'Genero: {genero}')
        break
    else:
        print('invalido...') 
    
  

cep_fisica = input('CEP.......................: ')
cep_fisica_f = '{}-{}'.format(cep_fisica[:5], cep_fisica[5:])
print(f'{cep_fisica_f}')
'''rua_fisica = str(input('Rua: '))
numero_fisica = str(input('Numero: '))
complemeto_fisica = input('Complemento: ')
bairro_fisica = input('Bairro: ')
cidade_fisica = input('Cidade: ')
uf_fisica = input('UF: ')
data_nascimento = int(input('Data de nascimento: '))
email_fisica = str(input('E-mail:'))

# cadastro de pessoa juridica
razao_social = str(input('Razão Social: '))
Nome_fantasia = str(input('Nome Fantasia: '))
cnpj = int(input('CNPJ: '))
atividade = str(input('Atividadde econômica: '))
cep_juridica = input('CEP: ')
rua_juridica = str(input('Rua: '))
numero_juridica = str(input('Numero: '))
complemeto_juridica = input('Complemento: ')
bairro_juridica = input('Bairro: ')
cidade_juridica = input('Cidade: ')
uf_juridica = input('UF: ')
data_fundação = int(input('Data de fundação: '))
email_juridica = str(input('E-mail:'))

# perguntas para perfil do cliente
'''