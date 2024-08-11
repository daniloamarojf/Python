# Cadastro de Cliente Pessoa Fisica
cpf_lista = []
genero_lista = []

def validar_cpf(cpf):
    if not cpf.isdigit() or len(cpf) != 11:  
        print('CPF inválido!')
        cpf = input('CPF.............................................: ') # nã0 esta jogando na lista
    else:
        cpf_lista.append(cpf) 
    return cpf

def validar_genero(genero):
    genero = str(input('Gênero M - Masculino | F - Feminino | O - Outros: ')).upper()
        
    if genero != 'M' or genero != 'F' or genero != 'o':
       print('invalido...') 
       genero = str(input('Gênero M - Masculino | F - Feminino | O - Outros: ')).upper() 
    elif genero == 'M':
        genero = 'Masculino'
        genero_lista.append(genero)
    elif genero == 'F':
        genero = 'Feminino'
        genero_lista.append(genero)
    else:
        genero = 'Outros'
        genero_lista(genero)

    return(genero)  
    
def cadastro():  
    
    nome = str(input('Nome............................................: '))

    cpf_lista = []
    cpf = input('CPF.............................................: ')
    validar_cpf(cpf)

    genero = str(input('Gênero M - Masculino | F - Feminino | O - Outros: ')).upper()
    validar_genero(genero)
         
        
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
        if len(rua) == 0 or rua.isnumeric():
            print('Digite o nome da rua') 
            continue
        
        break
        
    numero = int(input('Numero: '))

    complemeto = str(input('Complemento: '))
    bairro = input('Bairro: ')
    cidade = input('Cidade: ')
    uf = input('UF: ')
    data_nascimento = str(input('Data de nascimento: '))
    email = str(input('E-mail:'))

    return()

    # perguntas para perfil do cliente