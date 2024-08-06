# Crie uma função que receba a altura e o peso de uma pessoa. Depois retorne o seu IMC.

import os


os.system('cls')

def retornar_imc(altura, peso):
    
    imc = peso / (altura**2)
    print(f'{imc:.2f}')
    return(imc)

altura = float(input('Altura: '))
peso = float(input('Peso: '))

retornar_imc(altura, peso)