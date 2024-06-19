# Faça um programa que leia um número indeterminado de notas (pressione ‘s’ ou ‘0’ para sair). 
# Após esta entrada de dados, faça o seguinte:
# • Mostre a quantidade de notas que foram lidas.
# • Exiba todas as notas na ordem em que foram informadas.
# • Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra.
# • Calcule e mostre a soma das notas.
# • Calcule e mostre a média das notas.

import os


os.system('cls')

print('-'*70)
print('ENTRADA DE NOTAS')
print('-'*70)

soma = 0
contador = 1
lista = []
media = 0


while True:
    notas = (int(input('Número: ')))
    
    if notas == 0:
        # print('Fim do programa!')
        break
    
    soma += notas
    contador += 1
    lista.append(notas)
    media = soma/contador
# Quantidade de notas lidas
print()
print(f'Foram incluidas {contador} notas.')    
    
# Exiba todas as notas na ordem em que foram informadas
print(f'Notas: {lista}')
lista.reverse() 
   
# • Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra
print(f'A lista reversa é {lista}')

# • Calcule e mostre a soma das notas
print(f'A soma das notas é: {soma}')

# • Calcule e mostre a média das notas.
print(f'A média da notas é: {media}')
print()
print('Fim do programa!')

