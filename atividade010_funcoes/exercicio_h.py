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
    soma_altura = 0
    soma_peso = 0
    for clientes in cadastro:
        soma_altura += clientes ['altura']
        soma_peso += clientes ['peso']
        
        media_altura = soma_altura/len(cadastro)

        
        
        print(f'Soma das alturas: {soma_altura}, media {media_altura}')
    
def mostar_menu():
    print('Escolha a opção:')
    print('1 - Cadastrar')
    print('2 - Mostar cadastro')
    print('0 - sair') 
    
    return()

while True:
    mostar_menu()
    
    opcao = input('Qual opção: ')
    
    if opcao == 0:
        break
    
    elif opcao == 1:
        cadastrar()
        
    else:
        listar_dados() 
    
    
    










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
     
    
    

    


