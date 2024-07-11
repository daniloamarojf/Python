# Testando os comandos do python
# Dia: 15/04/2024

# Importando biblioteca
import os
import datetime

os.system('cls')

print('*' * 70 )
print('               Danilo Rogerio Magalhães Amaro              ')
print('*' * 70)

# Dados pessoais

print('Endereço: Rua Olimpio Costa, 145 - casa 2 - Benfica-JF')
print('CPF: 044.899.726-60')
print('Mãe: Maria da Aparecida Magalhães Amaro')
print('Pai: Rogerio Amaro')
print('')


ano_nascimento = input(int(f'Qual ano de nascimento: '))
ano_atual = datetime.datetime.now().year
idade = ano_atual - ano_nascimento


