import os


os.system('cls')

nomes = ['Agata', 'Bia', 'Coly', 'Isis']

for indice, nome in enumerate(nomes):
    # cria uma tupla contendo o indice e o nome da pessoa atual
    minha_tupla = (indice, nome)
    # A variável minha tupla e utilizada para acesar o
    # indice e o nome armazenado na tuplas
    # Mas posso acessar diretamente os elementos 'indice' e 'nomes
    print(f'O nome "{minha_tupla[1]}", posição {minha_tupla[0]} da lista.')
    print(f'O nome "{nome}", posição {indice} da lista.')
    print('-'*70)
    
    