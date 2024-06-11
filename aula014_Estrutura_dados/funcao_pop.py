import os


os.system('cls')

# Inicializa uma lista de exemplos
lista_numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Solicita ao usuários que unsira um indice para remover o elemento
indice = int(input('Digite o indice do elemento a ser removido (0-9): '))

# Verificar se o indice está dentro do intervalo válido da lista
if 0<= indice < len(lista_numeros):
    # Remove o elemento do indice especificado e exibi-o
    elemento_removido = lista_numeros.pop(indice)
    print(f'Elemento removido: {elemento_removido}')
else:
    print('Índice inválido!')
    
# Exibe a lista resultante
print('Lista após remoção:', lista_numeros)