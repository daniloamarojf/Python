# imports
# Biblioteca para interagir o SO
import os
# Biblioteca para pegar data e hora do sistema
import datetime


# limpar o terminal
os.system('cls')

print('-'*70)
print('ENTRADA DE DADOS EM PYTHON')               
print('='*70)

# Entrada
nome = input('Entre com um nome: ')
peso = input('Entre com o peso: ')
altura = input('entre com o altura:')

# entrada de casting
nascimento = int(input('Data de nascimento: '))
cep = int(input('Entre com o seu cep: '))
bairro = str(input('Entre com bairro: '))
rua = str(input('Nome da rua: '))
numero = int(input('Entre com o numero: '))

# Processamento: Pegando o ano corrente
ano_atual = datetime.datetime.now().year
idade = int(ano_atual) - nascimento

# Saida
print('-'*70)
print('SAIDA DE DADOS')
print('='*70)
print('Nome..............: ', nome)
print('Data de nascimento: ', nascimento)
print('Peso..............: ', peso)
print('Altura............: ', altura)

# saida interpolada
print(f'{nome}, você tem {idade} anos!')
print(f'CEP...............: {cep}')
print(f'Bairro............: {bairro}')
print(f'Rua...............: {rua}')
print(f'Numero............: {numero}')
print('-'*70)
print('')