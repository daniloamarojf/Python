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

def cadastrar():
    clientes ['codigo'] = str(input('Código: '))
    clientes ['nome'] = str(input('Nome: '))
    clientes ['altura'] = float(input('Altura: '))
    clientes ['peso'] = float(input('Peso: '))
  
    cadastro.append(clientes.copy())
    
    return()

def listar_dados():
    
    for clientes in cadastro:
        soma_altura += clientes ['altura']
        soma_peso += clientes ['peso']
        
        media_altura = soma_altura/len(cadastro)
    
    
    
    
    
    
    
    
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
     
    
    

    


