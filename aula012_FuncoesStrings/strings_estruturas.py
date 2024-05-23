import os


os.system('cls')
print('-'*70)
print('Operadores úteis para')
print('Strings e estrutura de dados')
print('-'*70)

texto = "Olá, Mundo!"

print(f'texto: {texto}')
if "Mundo" in texto: # Verifica a palavra dentro da string
    print('A palavra "Mundo" esta presente na string')
else:
    print('a palavra "Mundo não está presente na string')
    
print('-'*70)

texto2 = "Olá, Python!"

print(f'Texto2: {texto2}')
if "Mundo" not in texto2:    
    print('A palavra "Mundo" não está presente na string')
else:
    print('A palavra "Mundo" está presente na string')
    
print('-'*70)