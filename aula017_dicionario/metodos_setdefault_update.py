import os


os.system('cls')

meu_dicionario = {}

while True:
    print('-'*70)
    print('\nMenu de Opções:')
    print('1. Adicionar um par de chave-valor')
    print('2. Definir valor padrão para uma chave usando setdefault()')
    print('3. Atualizar o dicionário usando update()')
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
        # Definir valor padrão para uma chave usando setdefault()
        chave = input('Digite a chave para definir um valor padrão: ')
        valor_padrao = input('Digite o valor padrão: ')
        valor_existente = meu_dicionario.setdefault(chave, valor_padrao)
        print(f'Valor para chave "{chave}": {valor_existente}')
        
    elif opcao == '3':
        # Adicionar o dicionário usando update()
        novos_pares = input('Digite os novos pares chave_valor: ')
        novos_pares_listas = novos_pares.split(',')
        novos_dados = {}
        for par in novos_pares_listas:
            chave, valor = par.split(':')
            novos_dados[chave] = valor
        meu_dicionario.update(novos_dados) 
        print('Dicionário atualizado:', meu_dicionario)
        
    elif opcao == '4':
        # Mostrar o dicionário atual
        if meu_dicionario:
            print('Dicionário atual:', meu_dicionario)    
        else:
            print('O dicionário está vazio.')
            
    elif opcao == '5':
        # Sair do programa
        print('Saindo do programa.')
        break
    
    else:
        # Mensagem para opção invalida
        print('Opção inválida. Tente novamente.')
    