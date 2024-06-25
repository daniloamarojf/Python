import os
import re


os.system('cls')

print('Tipo de cliente: [1] Pessoa física [2] Pessoa juridica')
print()

# Condição para escolher se é cliente fisico ou juridico
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

cpf_lista = []

while True:
    cpf = input('CPF.............................................: ')
    if not cpf.isdigit() or len(cpf) != 11:  
        print('CPF inválido!')
        continue

    cpf_lista.append(cpf)
    # cep = input('cep: ')
    break


# validado gênero
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
    
cep_fisica_f = []  
while True:
    cep_fisica = input('CEP.......................: ')
    if not cep_fisica.isdigit() or len.cep_fisica != 8:
        print('CEP invalido') 
        continue
    
        
    
    cep_fisica_f = '{}-{}'.format(cep_fisica[:5], cep_fisica[5:])
    print(f'{cep_fisica_f}')
    break
    
    
    
rua_fisica = str(input('Rua: '))

numero_fisica = int(input('Numero: '))

complemeto_fisica = str(input('Complemento: '))
bairro_fisica = input('Bairro: ')
cidade_fisica = input('Cidade: ')
uf_fisica = input('UF: ')
data_nascimento = int(input('Data de nascimento: '))
email_fisica = str(input('E-mail:'))



# perguntas para perfil do cliente
