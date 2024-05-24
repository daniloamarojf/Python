# Faça um programa que receba uma frase e, em seguida, 
# mostre quantas vezes as vogais foram utilizadas.


import os


os.system('cls')

# Entrada de dados
frase = str(input('Digite uma frase: '))
a = 'a'
e = 'e'
i = 'i'
o = 'o'
u = 'u'
quantidade_a = frase.count(a)
quantidade_e = frase.count(e)
quantidade_i = frase.count(i)
quantidade_o = frase.count(o)
quantidade_u = frase.count(u)

# saida de dados
print(f'Esta frase possui {quantidade_a} vogais "a".')
print(f'Esta frase possui {quantidade_e} vogais "e".')
print(f'Esta frase possui {quantidade_i} vogais "i".')
print(f'Esta frase possui {quantidade_o} vogais "o".')
print(f'Esta frase possui {quantidade_u} vogais "u".')