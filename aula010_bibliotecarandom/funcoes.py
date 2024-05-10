import random
import os


os.system('cls')

print('-'*70)
print('BIBLIOTECA RANDOM')
print('-'*70)

print('Numero aleatorio')
numero_aleatorio = random.random()
print(f'O numero gerado foi {numero_aleatorio}')
print('-'*70)

print('Numero aleatorio inteiro')
aleatorio_inteiro = random.randint(1, 20)
print(f'O numero inreiro gerado é {aleatorio_inteiro}')
print('-'*70)

print('Numero aleatorio decimal no internvalo')
aleatorio_decimal = random.uniform(1, 10)
print(f'O numero decimal gerado foi: {aleatorio_decimal}')
print('-'*70)

print('Sorteio em uma lista')
lista = ['Agata', 'Coly', 'Isis', 'Bia']
nome_sorteado = random.choice(lista)
print(f'Lista: {lista}')
print(f'O nome escolhido foi: {nome_sorteado}')
print('-'*70)

print('Embaralhar sequência')
lista2 = ['Agata', 'Coly', 'Isis', 'Bia']
print(f'Lista antiga: {lista2}')
# Embaralhando = list(random.shuffle(lista)) dá erro
# Embaralhando = random.shuffle(lista) saida vazia
random.shuffle(lista2)
print(f'Lista nova: {lista2}')
print('-'*70)

print('Retorno de elementos únicos de uma população')
numeros = [1, 2, 3, 4, 5, 6, 7]
amostra_aleatoria = random.sample(numeros, 5)
print(f'Retorno da amostragem: {amostra_aleatoria}')
print('-'*70)

