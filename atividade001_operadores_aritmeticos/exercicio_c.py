# imports
import os

# Limpando tela
os.system('cls')

print('*'*70)
print(' Exercício "C" ')
print('*'*70)

# Entrada de dados 
nota_1 = float(input('Digite a primeira nota..: '))
nota_2 = float(input('Digite a segunda nota...: '))
nota_3 = float(input('Digite a terceira nota..: '))
nota_4 = float(input('Digite a quarta nota....: '))
print()
# Processamento
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

# Saída
print('-'*70)
print(' RESULTADO ')
print('-'*70)
print()
print(f'A média das notas é {media}')