import os


os.system('cls')

 
 # Definindo uma função
def calcular_velocidade_media(distancia, tempo, medida_d, medida_t):
    # Vm = deltaS/deltaT
    if medida_d == 'km' and medida_t == 'h':
        velocidade_media = distancia / tempo
        
    elif medida_d == 'm' and medida_t == 'min':
        velocidade_media = distancia / tempo
        
    return velocidade_media

distancia = float(input('Digite a distancia percorrida: '))
medida_d = input('Distancia em (km) ou (m)?:')

tempo = float(input('Digite o tempo gasto: '))
medida_t = input('Tempo em (h) ou (min)?: ')

# Calcular a velocidade média usando a função criada
velocidade = calcular_velocidade_media(distancia, tempo, medida_d, medida_t)

# Exibir o resultado
print(f'A velocidade média é {velocidade} {medida_d/medida_t}')
     