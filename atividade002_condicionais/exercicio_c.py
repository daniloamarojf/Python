# Curso de Desenvolvimento de Sistemas
# Turma: 0152
# Autor: Danilo Rogerio Magalhães Amaro
# Data: 26/04/2024
# Programa em Python para Empresa "SafeDrive"
# (Para monitoramento de velocidade)

import os


os.system('cls')

# Entrada de dados
print('.'*70)
print('Monitoramento de velocidade')
print('.'*70)
print()
velocidade = float(input('Digite a velocidade do veiculo (Km/h): '))
resposta = ''

# Condicionais
if velocidade > 60:
    resposta = 'Veículo ACIMA da velocidade permitida'
else:
    resposta = 'Veículo DENTRO da velocidade permitida'
    
# saida de dados
print('-'*70)
print(f'Veiculo a {velocidade} Km/h')
print(f'Atenção: {resposta}')
print('-'*70)
print('Fim do Programa')
