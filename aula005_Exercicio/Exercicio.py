# imports
# Biblioteca para interagir o SO
import os
# Biblioteca para utilizar data e hora do sistema
import datetime


# Lipamdo o terminal
os.system('cls')

print('*'*70)
print('DADOS DO VEICULO')
print('*'*70)

# Entrada de dados
propietario = input('Nome do Propietario: ')
veiculo = input('Veiculo: ')

# Entrada com casting
marca = str(input('Marca: '))
ano = int(input('Ano: '))
valor = float(input('Valor: '))
ipva_pago = False

# Processamento: pagando ano corrente
ano_atual = datetime.datetime.now().year
idade = int(ano_atual)-ano

# Saida
print(f'-'*70)
print(f'SAIDA DE DADOS DO VEICULO')
print(f'-'*70)
print(f'')
print(f'Sr(a) {propietario}, o {veiculo}, {marca}, {ano}')
print(f'possui valor atualizao de R$ {valor}')
print(f'')
print(f' * OBSERCAÇÃO')
print(f'IPVA pago: {ipva_pago}')
print(f'Este veículo possui {idade} anos de uso.')