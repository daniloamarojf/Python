import os


os.system('cls')

print('-'*70)
print('Fatiamento de strigs')
print('-'*70)

frase = 'String em Python'

# Exibindo a string original
print(f'String original: {frase}')

# Fatiamento: Acessando parte específica da string
# Primeiros cinco caracteres

primeiro_cinco = frase [:5]
print(f'Primeiros cinco caracteres: {primeiro_cinco}')

# Últimos dez caracteres
ultimos_dez = frase [-10:]
print(f'Últimos dez caracteres: {ultimos_dez}')

# Do quarto ao décimo caracters
quarto_ao_decimo = frase [3:10]
print(f'Do quarto ao décimo caracter: {quarto_ao_decimo}')

# A cada dois caracters
a_cada_dois = frase [::2]
print(f'A cada dois caracteres: {a_cada_dois}')

# Invertendo a String
invertida = frase[::-1]
print(f'String invertida: {invertida}')
print()
