# Trabalho sobre a extrutura de dados SET
# Senac Minas Gerais/Juiz de Fora
# Aluno: Danilo Amaro
# Turma: 0152
# Ano: 2024

# Lista atualizada

import os 


os.system('cls')

print('-'*50)
print(" RIFA  Números disponíveis")
print('-'*50)

rifa = set([1, 2, 3, 5, 6, 7, 8, 9, 10])

print()
print(rifa)
print()    
print('-'*50)
print('INFORME OS NÚMEROS VENDIDOS')
print('-'*50)
print()

 
    
   
for i in range (10): 
        
    num = int(input('Números vendidos: '))
    
    if num == 0:
        print()
        print('-'*50) 
        print('RIFA - Lista Atualizada')
        print('-'*50)
        print()
        break
    else:
         
        rifa.discard(num)
   
    
    
    
print(rifa)
print()