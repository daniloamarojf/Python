import os


os.system('cls')

# declaração
salario = int(input('Digite salario: '))
acrescimo = ''


if salario > 1500:
    acrescimo = salario * 0.05
elif salario < 1000:
    acrescimo = salario * 0.10
else:
    acrescimo = 0
    
salario_atual = salario + acrescimo    
# saida
print(f'o {salario} acescido de {acrescimo} é {salario_atual}')
