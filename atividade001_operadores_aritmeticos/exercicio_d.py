# imports
import os


# Limpando tela
os.system('cls')

print('*'*70)
print(' Exercício "D" ')
print('*'*70)

# Entrada
dividendo = float(input('Digite o dividendo: '))
divisor = float(input('Digite divisor......: '))
print()

# Processamento
quociente = dividendo / divisor
 
# Saida
print('-'*70)
print(' RESULTADO ')
print('-'*70)
print()
print(f'O resultado da divisão é: {quociente:.4f}')