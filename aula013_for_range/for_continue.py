import os


os.system('cls')

print('-'*70)
print('ESTRUTUARA DE CONTROLE: CONTINUE')
print('-'*70)

print()

for c in range(1, 11):
    if c == 5:
        # 5 está fora do loop, se retirar o numero abaixo,
        # ele não aparecerá na saida, deixei para verificação!
        print(f'O número {c} está fora do loop')
        continue  # salta  e o ciclo continua
    
    print(f'o número é {c}')
    
print('-'*70)
print()