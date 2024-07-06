# Trabalho sobre a extrutura de dados SET
# Senac Minas Gerais/Juiz de Fora
# Aluno: Danilo Amaro
# Turma: 0152
# Ano: 2024

# Método discard()

# Importando biblioteca
import os 


os.system('cls')

# Rifa com 30 números para venda
print('-'*55)
print(" RIFA - Número ")
print('-'*55)

rifa = set([1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])

print()
print(rifa)
print() 

# Solicitando ao usuário que informe os números vendidos   
print('-'*55)
print('INFORME OS NÚMEROS VENDIDOS ou digite "00" para sair')
print('-'*55)
print()

for i in range (10): 
        
    num = int(input('Números vendidos: '))
    
    if num == 00:
        
        break
    else:
        # Usando o metódo discard para remover os números vendidos
        rifa.discard(num) 
         
# Imprimindo Rifa atualizada, com números a serem vendidos    

print()
print('RIFA - Números disponíveis')
print()      
print(rifa)
print()