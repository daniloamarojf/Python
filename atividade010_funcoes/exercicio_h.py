# Uma Academia deseja fazer uma pesquisa entre seus clientes para descobrir
# a média de altura  e peso de seus clientes. Faça um programa que pergunte a
# cada um dos clientes da academia seu código, nome, altura e peso.
# Após esse cadastramento, seu programa deverá listar os dados dos clientes e a média.
# Para sair do programa o usuário deverá digitar o valor zero(0). 
# O número de clientes é indefinido. Veja a saída no próximo slide.

def limpar_tela():
    import os
    os.system('cls')
    
    
def firula():
    print('-'*50)
    
limpar_tela()
firula()
print('Pesquisa em Academia')
firula()

clientes = {}
cadastro = []

def cadastrar(cadastro):
    codigo = str(input('Código: '))
    nome = str(input('Nome: '))
    altura = float(input('Altura: '))
    peso = int(input('Peso: '))
    cliente = {'codigo': codigo, 'nome': nome, 'altura': altura, 'peso': peso}
    
    cadastro.append(cliente)
    
    return(cadastro)

cadastrar()
'''while True:
    print('1 - Cadastrar')
    print('2 - Visualizar')
    print('0 - Sair')
    firula()
    opcao = input('Digite a opção: ')
    firula()
    
    if (opcao == 0):
         break
    elif (opcao == 2):
        '''
     
    
    

    


