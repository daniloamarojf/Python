# Trabalho sobre a extrutura de dados SET
# Senac Minas Gerais/Juiz de Fora
# Aluno: Danilo Amaro
# Turma: 0152
# Ano: 2024

# Lista atualizada

import os 


os.system('cls')

doacoes = []

print('-'*50)
print(" LISTA DE DOAÇÕES ")
print('-'*50)

for i in range(3):
    item = (input(f'{i + 1} -  '))
    doacoes.append(item)
    
print(doacoes)

while True:
    remover = input('Itens já doados: ')
    doacoes.discard(remover)