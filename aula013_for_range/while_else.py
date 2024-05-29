import os


os.system('cls')


print('-'*70)
print('ESTRUTURA DE CONTROLE WHILE ELSE BREAK')
print('-'*70)

print()

while (True):
    # lower() garante o tratamento para entrade de s ou S
    nome = str(input('Digite um nome [s - Sair]: ').lower())
    
    if (nome != 's'):
        print('continue digitando ...')
    else:
        print('-'*70)
        print('Você digitou "s" para sair!')
              
        # interrompe o laço
        break
              
              
