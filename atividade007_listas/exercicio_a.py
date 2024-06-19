# Faça um programa que leia um número indeterminado de notas (pressione ‘s’ ou ‘0’ para sair). 
# Após esta entrada de dados, faça o seguinte:
# • Mostre a quantidade de notas que foram lidas.
# • Exiba todas as notas na ordem em que foram informadas.
# • Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra.
# • Calcule e mostre a soma das notas.
# • Calcule e mostre a média das notas.

import os

soma = 0
contador = 1
lista = []
lista_reversa = []

os.system('cls')

while True:
    notas = input('Número: ')
    
    if notas == '0' or notas == 's':
        print('Fim do programa!')
        break
    
    contador += 1
    print(f'Foram incluidas {contador} notas.')    
    
    if 
    lista = notas.split()
    
    print(f'Notas: {lista}')
    
    '''if i in lista:
    
    lista.append(i)
    
    
    
    lista_reversa.reverse(lista)
    

print(f'Notas {lista}')
print(f'A lista reversa é {lista_reversa}')'''