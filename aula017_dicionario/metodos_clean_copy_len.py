import os


os.system('cls')
# criação do dicionário vazio
meu_diconario = {}

while True:
    print('-'*70)
    # Exibição do menu de opções
    print('\nMenu de opções:')
    print('1. Adicionar um par de chave-valor')
    print('2. Mostrar o dicionário')
    print('3. Mostrar o tamanho do dicionário')
    print('4. Fazer uma cópia do dicionário')
    print('5. Limpar o dicionário')
    print('6. Sair')
    print('-'*70)
    
    # Solicitação da escolha do usuário
    opcao = input('Escolha uma opção (1-6): ')
    
    if opcao == '1':
        # Adiciona um novo par de chaves ao dicionário
        chave = input('Digite a chave: ')
        valor = input('Digite o valor: ')
        meu_diconario[chave] = valor
        print(f'Para {chave}: {valor} adicionado.')
        
    elif opcao == '2':
        # Exibe o dicionário atual
        print('Dicionário atual:', meu_diconario)
        
    elif opcao == '3':
        # Mostra o tamanho do dicionário usando len()
        tamanho = len(meu_diconario)
        print(f'O dicionário tem {tamanho} elementos.')
        
    elif opcao == '4':
        # Cria uma cópia do dicionário usando copy() e exibe a cópia
        copia_dicionario = meu_diconario.copy()
        print(f'Cópia do dicionário:', copia_dicionario)
        
    elif opcao == '5':
        # Limpa o dicionário usando o clean()
        meu_diconario.clear()
        print('Dicionário limpo')
        
    elif opcao == '6':
        # sair do programa
        print('Saindo do programa.')
        break
        
    else:
        # Mensagem para opção inválida
        print('Opção inválida. Tente novamente.')