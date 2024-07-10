import os


os.system('cls')
numero_lista = []
numero = input('Número: ')

if numero == 0:
    print('Número inválido!')
    
else:
    numero_lista.append(numero)

print(f'{numero}')