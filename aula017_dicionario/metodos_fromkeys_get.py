import os


os.system('cls')

meu_diconario = None

# Loop principal do programa
while True:
    print('-'*70)
    print('\nMenu de opções:')
    print('1. Crir dicionário com fromkeys()')
    print('2. Buscar valor de uma chave com get()')
    print('3. Sair')
    print('-'*70)
    
    opcao = input('Escolha uma opção (1-3):')
    
    if opcao == '1':
        # Criação de um dicionário usando framkeys
        chaves = input('Digite as chaves separadas por vírgula: ').split(',')
        valor_padrao = input('Digite o valor padão para as chaves: ')
        meu_diconario = dict.fromkeys(chaves, valor_padrao)
        print('Dicionário criado:', meu_diconario)
        
    elif opcao == '2':
        # Verificar se o dicionário foi criado antes de tentar acessa-lo 
        if meu_diconario is not None:
            chave = input('Digite as chave que deseja buscar: ')
            valor = meu_diconario.get(chave, "Chave não encontarada")
            print(f'Valor para a chave "{chave}": {valor}') 
        else:
            print('Erro! Crie um dicionário.')
    
    elif opcao == '3':
        print('Saindo do programa.')    
        break
        
    else:
        print('Opção inválida. Tente novamente.')
        