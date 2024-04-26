# Curso de Desenvolvimento de Sistemas
# Turma: 0152
# Autor: Danilo Rogério Magalhães Amaro
# Data: 25/04/2024
# Estudo de Condicionais: Parte 4
# Operadores Lógicos

import os


# Limpando o terminal
os.system('cls')

# Declaração
a = 10
b = 5
c = 'Jhon'

print('-'*70)
print('Condicionais: Operadores Lógicos')
print('='*70)

# E (and) Verdadeiro
print('E (and) VERDADEIRO')
if (a > 5 and b != c):
    print('Verdadeiro: Bloco execultado')
else:
    print('Falso: Bloco execultado')
    
print('-'*70)

# E (and) FALSO
print('E (and) FALSO')
if (a > 5 and b == c):
    print('Verdadeiro: Bloco execultado')
else:
    print('Falso: Bloco execultado')
    
    print('.'*70)
    
# OU (or) VERDADEIRO
print('OU (or) VERDADERIO')
if (a > 5 or b == c):
    print('Verdadeiro: Bloco execultado')
else:
    print('Falso: Bloco execultado')
    
print('.'*70)

# OU (or) FALSO
print('Ou (or) FALSO')
if (a < 5 or c == 'Jane'):
    print('Verdadeiro: Bloco execultado')
else:
    print('FALSO: Bloco execultado')
print('-'*70)
print()