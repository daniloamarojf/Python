import os


os.system('cls')


print('-'*70)
print('COMANDO WHILE')
print('-'*70)

print()

contador = 1

while contador < 7:
    print('Contador é:', contador)
    contador += 1
    
    # se eu tiver essa condicional o else será execultado
    if contador == 4:
        print(f'Contador chegou em {contador}. Break no while!')
        break
    
else: 
    print('While finalizado!')    
    
print()
    
