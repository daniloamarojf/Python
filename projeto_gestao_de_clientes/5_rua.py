import os


os.system('cls')

rua_lista = []

while True:           
    rua = str(input('Rua: ')).capitalize()
    if len(rua) == 0 or rua.isnumeric():
        print('Digite o nome da rua') 
        continue
    
    break
