# Crie uma função que receba a altura e o peso de uma pessoa. Depois retorne o seu IMC.

import os


os.system('cls')

print('-'*50)
print('Calculando o IMC')
print('-'*50)

def retornar_imc(altura, peso):
    
    imc = peso / (altura**2)
    print(f'O Índice de Massa Corporal é: {imc:.2f}')
    return(imc)

altura = float(input('Informe sua Altura: '))
peso = float(input('Informe seu Peso: '))

retornar_imc(altura, peso)