import csv
import os


# Nome  do arquivo CSV
arquivo = "arquivos_csv/gravacao/alunas.csv"

# Lista para armazenar os dados
lista = []

# Abrindo o arquivo CSV para leitura
with open(arquivo, 'r') as arquivo_csv:
    # Criando um leitor de CSV qe lê o arquivo como dicionário
    leitura = csv.DictReader(arquivo_csv, delimiter=';')
    
    # Interando sobre cada linha (registro) no arquivo CSV e adicionando da lista
    for linha in leitura:
        lista.append(linha)
        
os.system('cls')
print('-'*70)
print('nome\ttelefone\tcidade')
print('='*70)
# Exibindo a lista resultante
for registro in lista:
    flag = 0
    for k, v in registro.items():
        print(v, end='\t')
        flag +=1
        if flag == 3:
            print()
print('-'*70)