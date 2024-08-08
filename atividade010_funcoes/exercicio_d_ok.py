# Crie uma função que receba uma temperatura em fahrenheit e retorne o valor em graus célsius.

# importando biblioteca
import os


os.system('cls')

temp_celsius = 0
temp_fahrenheit = 0


# criando função conversão de temperatura
def mudar_temperatura(temp_fahrenheit):
    
    temp_celsius = (temp_fahrenheit - 30)/2 # Formula conversão faharenheit em celsius
    return temp_celsius

print('-'*50)
print('Conversão de temperatura')
print('-'*50)
print()
temp_fahrenheit = float(input('Imforme a temperatura em f: '))

print(f'A temperatura {temp_fahrenheit}F equivale a {mudar_temperatura(temp_fahrenheit):.2f}C')

'''import os


os.system('cls')

def mudar_temperatura(temp_fahrennheit):
    temp_celsius = (temp_fahrennheit - 32)/1.8
    return temp_celsius

print('-' * 70)
print('CONVERSÃO DE TEMPERATURA')
print('=' * 70)

temp_fahrennheit = float(input('Informe a temperatura: '))
print(f'A temperatura {temp_fahrennheit} em Célsius é {mudar_temperatura(temp_fahrennheit):.2f}')'''