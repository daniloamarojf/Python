import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE DADOS: list comprehension')
print('='*70)

lista_numeros = [100, 200, 300, 400, 500, 600]

# valores com juros
lista_com_juros = []

for item in lista_numeros:
    
    lista_com_juros.append(item + (item * .10))
    
print('Aplicar 10% de juros: Forma normal')
print(f'Lista com juros: {lista_com_juros}')
print()

# list comprehension
lista_com_juros_2 = [item + (item * .10) for item in lista_numeros]
print('Aplicar 10% juros: list comprehension')
print(f'Lista com juros: {lista_com_juros_2}\n')