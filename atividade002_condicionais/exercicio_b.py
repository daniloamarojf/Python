# Curso de Desenvolvimento de Sistemas
# Turma: 0152
# Autor: Danilo Rogerio Magalhães Amaro
# Data: 25/04/2024
# Programa em Python para Empresa "DataMax"
# (Para inserir 3 numero e determinar (>,<,=))

import os


os.system('cls')

a = float(input('Digite o 1º numero'))
b = float(input('Digite o 2º numero'))
c = float(input('Digite o 3º numero'))

if a == b and b == c:
    numero = ('Os numeros são iguais!')
elif a > b and a > c:
    numero= ('O numero a é maior')
elif b > a and b > c:
    numero = ('O numero b é maior')
else:
    numero = ('O numero c é maior')
    

if a < b and a < c:
    numero1 = ('O numero a é menor')
elif b < a and b < c:
    numero1 = ('O numero b é menor')
else:
    numero1 = ('O numero c é menor')
    
print()
print(f'{numero}')
print(f'{numero1}')
