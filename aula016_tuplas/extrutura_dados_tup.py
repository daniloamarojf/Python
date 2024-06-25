# solicitar ao usuário a quantidade de elementos da tupla
import os


os.system('cls')

# Solicitar ao usuário a quantide de elementos da tupla
numero_elementos = int(input('Quantos elementos na tupla? '))

# Inicializar um lista vazia para armazenar os elementos
elementos = []

# Estrutura de repetição para obter os elementos do usuário
for i in range(numero_elementos):
    while True:
        valor = input(f'Digite o valor {i + 1}: ')
        if valor.isdigit(): # Verificar se a entrada é um número
            elementos.append(int(valor))
            break
        else:
            print('Entrada invalida. Digite um número')
            
# Converter a lista em uma tupla
tupla = tuple(elementos)

print('-'*70)
# Exibir a tupla criada
print(f'Tupla crianda: {tupla}')
print('-'*70)

# Extrutura de repetição para permitir múltiplas
# operações até que usuário deseje sair
while True:
    # Condicional para verificar
    # um número específico
    valor = int(input('Verificar se o numero da tupla: '))
    
    if valor in tupla:
        print(f'O número {valor} está na tupla.')
        # Contar quantas vezes o numero aparece
        contagem = tupla.count(valor)
        print(f'O número {valor} aparece {contagem} vez(es).')
        # encontar o ídice da primeira ocorrência
        
        indice = tupla.index(valor)
        print(f'A primeira ocorrência de {valor} está no índice {indice}.')
        
    else:
        print(f'O número {valor} não está na lista.')
        
        # Perguntar ao usuário se deseja realizar
        # outra operação ou sair
        
    continuar = input('Deseja continuar (s/n): ').lower()
    if continuar != 's':
        print('Encerrando o programa. Até mais!')
        break
print('-'*70)    
print('Fim do programa!')
print('-'*70)