# Faça um programa que leia as vogais, depois mostre-as em ordem inversa.
import os 

os.system('cls')
print('-'*70)
print('VOGAIS INVERSA')
print('-'*70)

# declaração
vogais = ['a', 'e', 'i', 'o', 'u']

# invertendo as vogais
inversao = vogais[::-1]

print()
print(f'Vogais: {vogais}')
print()
print(f'Vogais inversa: {inversao}')
