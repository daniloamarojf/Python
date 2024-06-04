# Faça um algoritmo que imprima a frase "estou em looping" e, em seguida, 
# solicite ao usuário digitar uma letra. Caso a letra seja o “f" finalize a aplicação.
# Do contrário, imprima novamente a mesma frase até que o caractere “f" seja digitado.

import os


os.system('cls')

frase = '"Estou em looping"'

print('-'*70)
print('"Estou em looping"')
print('-'*70)
print()

while (True):
    sair = str(input('Digite uma letra para finalizar: ')).lower()
    print()
    
    if (sair != 'f'):
        print(f'{frase}')
    else:
        print()
        print('Operação finaizada!')
        print()
        break