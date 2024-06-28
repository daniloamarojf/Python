import os


os.system('cls')


print('-'*70)
print('----------TABELA PERIÓDICA---------')
print('='*70)

# Inicialização do dicionário e da lista
elementos = {}
periodica = []

while True:
    os.system('cls')
    
    # cabeçalho do menu
    print('-'*70)
    print('MENU DE OPÇÕES:')
    print('='*70)
    print('1. Adicionar um elemento')
    print('2. Visualizar todos os elementos')
    print('3. Atualizar um elemento')
    print('4. Remover um elemento')
    print('5. Sair')
    print('-'* 70)
    
    # Solicitação da escolha do usuário
    opcao = str(input('Escolha uma opção (1-5): '))
    
    if opcao == '1':
        # Adicionar um elemento
        simbolo = str(input('Simbolo do elemento: '))
        nome = str(input('Nome do elemento: '))
        elementos['simbolo'] = simbolo
        elementos['nome'] = nome
        periodica.append(elementos.copy())
        input('\nElemento adicionado. Pressione enter para continuar...')
        
    elif opcao == '2':
        # Visualizar todos os elementos
        print('\nElementos na tabela periódica:')
        print('-' * 70)
        for elemento in periodica:
            for chave, valor in elementos.items():
                print(f'{chave.capitalize()}: {valor}')
            print('-' * 70)
        input('\nPressione Enter para continuar ...')
    
    elif opcao == '3':
        # Atualizar um elementos
        simbolo = str(input('Digite o símbolo do elemento para atualizar: '))
        # inicializa a flag como False
        encontrado = False
        for elemento in periodica:
            if elemento['simbolo'] == simbolo:
                novo_simbolo = str(input('Digite o novo símbolo para'
                f'{simbolo} (ou deixe em branco para manter o atual: )'))
                novo_nome = str(input('Digite o novo nome para'
                f' {nome} (ou deixe em branco para manter o atual)'))
                
                # Atualizar o simbolo e o nome se fornecido
                if novo_simbolo:
                    elemento['simbolo'] = novo_simbolo
                if novo_nome:
                    elemento['nome'] = novo_nome
                # Define a flag coo True quando o elemento é encontrado
                encontrado - True
                break
                
        if encontrado:
            input('\nElemento atualizado. Enter para continuar...')
        else:
            input('\nElemento não encontrado. Enter para continuar...')
    
    elif opcao == '4':
        # remover um elemento
        simbolo = str(
            input('Digite o símbolo do elemento que deseja remover:'))        
        encontrado = False # inicializa a flag com false
        for elemento in periodica:
            if elemento['simbolo'] == simbolo:
                periodica.remove(elemento)
                # define flag como True quando o elemento é encontrado
                encontrado = True
                break
            if encontrado:
                input('\nElemento removido. Enter para continuar...')
            else:
                input('\nElemento não encontrado. Enter para continuar...')
                
    elif opcao == '5':
        print('Saido do programa.')
        break
    
    else:
        input('Opção inválida. Enter para tentar novamente...')
        
