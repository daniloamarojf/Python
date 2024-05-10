# Importando as bibliotecas
import os
# Podemos importar somente as funções que queremos utilizar
from datetime import datetime
from datetime import date


# Limpando o terminal
os.system('cls')

# Declarando uma variavel para data
data = datetime.now()

# Declarando uma variável data formatada
data_formatada = date.strftime('%d/%m/%Y')

# Declaração de uma variavel data e hora formatada
data_hora_formatada = date.strftime('%d/%m/%Y %H:%M')

print(f'Data formatada : {data_formatada}')
print(f'Data e hora formatadas: {data_hora_formatada}')

# Recebendo o ano
data_atual = date.today()
nascimento = 1970
idade = data_atual.year - nascimento

# Imprimindo a data atual e o nascimento
print('-'*70)
print(f'Data atual do sitema: {data_atual}')
print(f'Nascimento..........: {nascimento}')
# imprimindo somente o ano
print(f'Ano atual............: {data_atual.year}')
# Imprimindo somente a idade
print(f'Sua idade é..........: {idade} anos')
print('-'*70)
