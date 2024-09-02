import os
from gestao_clientes.pessoa_fisica import cadastro


os.system('cls')

while True:
    print('Tipo de clinete: [1] Pessoa Física [2] Pessoa Juridica')
    print()
    cliente = input('Tipo clinte......................................: ')
    
    if cliente == '1' or cliente == '2':
        if cliente == '1':
            cadastro()
        else:
            cliente = 'Pessoa Juridica'
            
    else:
        print('Digite 1 para pessoa fisica ou 2 para pessoa juridica')
        
        break
    