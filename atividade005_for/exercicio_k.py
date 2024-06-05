# Crie um programa que pede que o usuário digite um nome ou uma frase,
# verifique se esse conteúdo digitado é um palíndromo ou não,
# exibindo em tela esse resultado.

import os


os.system('cls')

frase = input('Frase: ').upper()
frase_inverso = frase[::-1].upper()
print()
print(f'Frase original: {frase}')
print(f'Frase inversa: {frase_inverso}')
print()

if frase in frase_inverso:
    print('Texto "é" um polídromo')
else:
    print('Texto "não" é polídromo')
