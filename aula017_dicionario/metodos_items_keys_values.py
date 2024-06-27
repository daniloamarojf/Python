import os


os.system('cls')

meu_dicionario = {}

while True:
    print('-'*70)
    print('\nMenu de Opções:')
    print('1. Adicionar u par de chave-valor')
    print('2. Mostrar chaves do dicionário')
    print('3. Mostrar valores do dicionário')
    print('4. Mostar itens do dicionário')
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
        # Mostsr as chaves do dicionário usando keys()
        if meu_dicionario:
            print('Chaves do dicionário:', meu_dicionario.keys())
        else:
            print('O dicionário está vazio. Adicione itens primeiro.')
            
    elif opcao == '3':
        # Mostar os valores do dicionário usando valeus
        if meu_dicionario:
            print('Valor do dicionário:', meu_dicionario.values())
        else:
            print('o dicionário está vazio. Adicione itens primeiro.')
            
    elif opcao == '4':
        # Mostar os itens (chave-valor) do dicionário usando itens
        if meu_dicionario:
            print('Itens do dicionário:', meu_dicionario.items())
        else:
            print('o dicionário está vazio. Adicione itens primeiro.')
            
    elif opcao == '5':
        # Sair do programa
        print('Saindo do programa.')
        break
    
    else:
        # Mensagem para opção inválida
        print('Opção inválida. Tente novamente.')