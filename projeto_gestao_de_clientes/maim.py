import os


os.system('cls')
from gestao_clientes.pessoa_fisica.cadastro import cadastro

print('Tipo de cliente: [1] Pessoa física [2] Pessoa juridica')
print()

# Condição para escolher se é cliente fisico ou juridico
while (True):
    cliente = int(input('Tipo cliente....................................: '))
    
    if cliente == 1 or cliente == 2:
        if cliente == 1:
            cadastro()
        else:
            cliente = "Pessoa Juridica"
        break 
    else:
        print('Digite 1 para pessoa física ou 2 para pessoa juridica')
        
print(f'Cliente.........................................: {cliente}')

