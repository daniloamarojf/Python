import os


os.system('cls')

cpf = int(input('Digite cpf: '))

while True:
    if len(cpf) == 11:
        break
    else:
        print('cpf valido')