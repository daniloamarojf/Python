# imports
import os


# Limpando a tela
os.system('cls')

print('*'*70)
print(' Exercício "E" ')
print('*'*70)

# Entrada de dados
numero = int(input('Digite um numero: '))
print()

# Processamento
antecessor = numero - 1
sucessor = numero + 1

# Saída
print('-'*70)
print(' RESULTADO ')
print('-'*70)
print(f'O antecessor de {numero} é {antecessor} e o '
      f'sucessor  {sucessor}')