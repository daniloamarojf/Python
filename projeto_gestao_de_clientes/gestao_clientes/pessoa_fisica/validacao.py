def validar_cpf(cpf):
    cpf_lista = []
    if not cpf.isdigit() or len(cpf) != 11:  
        print('CPF inválido!')
        cpf = input('CPF.............................................: ') 
        cpf_lista.append(cpf) 
    return cpf

def validar_genero(genero):
    genero_lista = []
        
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

    return genero  

def validar_cep(cep):
    cep_lista = []  
    
    posicao = cep.find('-')
        
    if (not cep.isdigit) or len(cep) != 9 or posicao != 5:
        print('"CEP" invalido. Formato deve ser 00000-000') 
    else:
        
        cep_lista.append(cep)
        
    return cep

def validar_rua(rua):
    rua_lista = []

    if len(rua) == 0 or rua.isnumeric():
        print('Digite o nome da rua') 
    else:    
        rua_lista.append(rua)
        
    return rua