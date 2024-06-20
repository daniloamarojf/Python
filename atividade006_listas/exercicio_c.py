# Faça um programa que procure na lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# e produza:
'''• O intervalo de 1 até 9
• O intervalo de 8 até 13
• Os números pares
• Os números ímpares
• Os múltiplos de 2, 3 e 4
• Lista reversa
• O produto dos intervalos 5-6 por 11-12'''

import os 


os.system('cls')
multiplos_2 = []
multiplos_3 = []
multiplos_4 = []
produto = []

# declaração
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
intervalo_1a9 = numeros[0:10]
intervalo_8a13 = numeros[7:13]
numeros_pares = numeros[1:15:2]
numeros_impares = numeros[0:15:2]
lista_reversa = numeros[::-1]
intervalo5_6 = numeros[4:5]
intervalo11_12 = numeros[10:11]

for i in numeros:
    
    if i % 2 == 0:
        multiplos_2.append(i)

for i in numeros:
    if i % 3 == 0:
        multiplos_3.append(i)
        
for i in numeros:
    if i % 4 == 0:
        multiplos_4.append(i)

for i in (intervalo5_6):
    for j in (intervalo11_12):
        produto.append(i * j)


print(f'Numeros: {numeros}')
print()
print(f'Intervalo entre 1 e 10: {intervalo_1a9}')
print(f'Intervalo entre 8 e 13: {intervalo_8a13}')
print(f'Números pares: {numeros_pares}')
print(f'Números multiplos de 2: {multiplos_2}')
print(f'Números multiplos de 3: {multiplos_3}')
print(f'Números multiplos de 4: {multiplos_4}')
print(f'Números reverso: {lista_reversa}')
print(f'Produto dos intervalos: {produto}')