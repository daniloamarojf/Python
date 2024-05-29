import os


os.system('cls')

soma = 0

for c in range(0, 5):
    
    numero = input('Digite um numero [0-5]: ')
    
    # validação
    if (not (numero.isnumeric())):
        print(f'"{numero}" Entrada invalida!')
        print()
    else:
        # casting d variável, ou seja, vai virar um inteiro
        numero = int(numero)  
        
        # validando o intervalo pedido
        if (numero>=0 and numero<=5):
            print(f'O número {numero} está dentro do intervalo [0-5]!')  
            print()
        else:
            print(f'"{numero}" Entrada inválida!')
            print()

print('-'*70)
print()