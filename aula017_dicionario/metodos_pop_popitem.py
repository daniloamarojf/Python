import os


os.system('cls')

meu_dicionario = {}

while True:
    print('-'*70)
    print('\nMenu de Opções:')
    print('1. Adicionar um par de chave-valor')
    print('2. Remover um item usando pop()')
    print('3. Remover o último item usando popitem()')
    print('4. Mostar dicionário atual')
    print('5. Sair')
    print('-'*70)
    
    opcao = input('Escolha uma opção (1-5): ')
    
    if opcao == '1':
        # Adicionar um par de chave-valor ao dicionário
        chave = input('Digite a chave: ')
        valor = input('Digite o valor: ')
        meu_dicionario[chave] = valor
        print(f'Par {chave}: {valor} adicionado.')
        
    elif opcao == '2':
        # Remover um item específico usando pop()
        if meu_dicionario:
            chave = input('Digite e chave do item que deseja remover:')
            valor_removido = meu_dicionario.pop(chave, "Chave não encontrada!")
            print(f'Item removido: {chave}: {valor_removido}')
        else:
            print('O dicionário está vazio. Adicione itens primeiro.')
            
    elif opcao == '3':
        # Remover o último item usando popitem()
        if meu_dicionario:
            chave, valor = meu_dicionario.popitem()
            print(f'Último item removido: {chave}: {valor}')
        else:
            print('o dicionário está vazio. Adicione itens primeiro.')
            
    elif opcao == '4':
        # Mostar o dicionário atual
        if meu_dicionario:
            print('Dicionário atual:', meu_dicionario)
        else:
            print('O dicionário está vazio.')
            
    elif opcao == '5':
        print('Saindo do programa.')
        break
    
    else:
        # Mensagem para opção inválida
        print('Opção inválida. Tente novamente.')