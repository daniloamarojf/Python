import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE CONTROLE WHILE ELSE CONTINUE')
print('-'*70)

print()

contador = 0 # flag

while (contador <= 10):
    
    # soma o contador
    contador += 1 # é o mesmo que contador = contador + 1
    
    if (contador % 2 == 0): # pulando os pares
        continue
    print(f'Contador = {contador}')
else:
    print(f'Bloco do While...else: contador em {contador}!')
    
print('-'*70)
print('Fim do programa!')
print()