import os
import re


os.system('cls')

cep_fisica_f = []  
while True:
    cep_fisica = input('CEP.......................: ')
    posicao = cep_fisica.find('-')
    
    if (not cep_fisica.isdigit) or len(cep_fisica) != 9 or posicao != 5:
        print('CEP invalido. Formato deve ser 00000-000') 
        continue
    
    cep_fisica_f.append(cep_fisica)
    
    break