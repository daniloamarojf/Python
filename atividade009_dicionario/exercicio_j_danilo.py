# Faça um programa para criar um dicionário com nomes de frutas.
# Em seguida verifique se tem abacaxi nos valores.
import os

os.system('cls')

print('-'*50)
print('DICIONÁRIO DE FRUTAS')
print('-'*50)

frutas = {}
frutas_valor = {}

for i in range(5):
    # Adicionando Chaves:valor ao dicionário
    chave = (f'Fruta{i+1}')
    valor = (input(f'Digite Fruta{i+1}: ')).upper
    frutas[chave] = valor
    
    frutas_valor = frutas.values() 

print('-'*60)
print('DICIONÁRIO:')    
print(f'{frutas}')
print('-'*60) 
print()   

if 'abacaxi' in frutas_valor:
    print(f'------> Contém Abacaxi na lista.')
else:
    print('------> Não contém abacaxi na lista.')  
 

   
    