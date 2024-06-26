# Trabalho sobre a extrutura de dados SET
# Senac Minas Gerais/Juiz de Fora
# Aluno: Danilo Amaro
# Turma: 0152
# Ano: 2024

# Lista atualizada

import os 


os.system('cls')

print('-'*50)
print(" LISTA DE DOAÇÕES ")
print('-'*50)

doacoes = set([])
itens_remover = set([])

for i in range(3):
    item = (input(f'{i + 1} -  '))
    doacoes.add(item)

print()    
print('-'*50)
print('INFORME OS INTENS JÁ DOADOS')
print('-'*50)
print()
print(doacoes)

while True:
    
    remover = input('Itens já doados: ').lower
    itens_remover.add(remover)
    
    for itens_remover in doacoes:    
        doacoes.discard(itens_remover)
    else:
        print('fim')
    break
    
print(doacoes)