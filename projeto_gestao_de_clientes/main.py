import os
from gestao_clientes.pessoa_fisica import cadastro

os.system('cls')



# Condição para escolher se é cliente fisico ou juridico
while True:
    print('Tipo de cliente: [1] Pessoa física [2] Pessoa juridica')
    print()
    cliente = (input('Tipo cliente....................................: '))
    
    
    
    if cliente == '1' or cliente == '2':
        if cliente == 1:
            cadastro()
        else:
            cliente = "Pessoa Juridica"
         
    else:
        print('Digite 1 para pessoa física ou 2 para pessoa juridica')
    break