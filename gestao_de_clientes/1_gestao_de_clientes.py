import os


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
    
cep_lista = []  
while True:
    cep = input('CEP.......................: ')
    posicao = cep.find('-')
    
    if (not cep.isdigit) or len(cep) != 9 or posicao != 5:
        print('"CEP" invalido. Formato deve ser 00000-000') 
        continue
    
    cep_lista.append(cep)
    
    break

rua_lista = []

while True:           
    rua = str(input('Rua: ')).capitalize()
    if len(rua) == 0:
        print('Digite o nome da rua') 
        continue
    
    break
    
numero = int(input('Numero: '))

complemeto = str(input('Complemento: '))
bairro = input('Bairro: ')
cidade = input('Cidade: ')
uf = input('UF: ')
data_nascimento = int(input('Data de nascimento: '))
email = str(input('E-mail:'))



# perguntas para perfil do cliente
