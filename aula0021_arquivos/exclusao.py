import csv
import os


os.system('cls')

arquivo = 'arquivos_csv/gravacao/alunas.csv'
nome_para_apagar = input('Digite o nome que deseja apagar:')

# Lendo os dados do arquivo
with open(arquivo, 'r') as arquivos_csv:   # erro#######
    leitura = csv.DictReader(arquivos_csv, delimiter=';')
    cadastro = list(leitura)
    
# Verificando se o nome existe e apagando o registro
apagado = False
novo_cadastro = [registro for registro in cadastro \
                 if registro['nome'] != nome_para_apagar]

if len(novo_cadastro) < len(cadastro):
    apagado = True
    
# Reescrevendo o arquivo com os dados atualizados
with open(arquivo, 'w', newline='') as aquivos_csv:
    campos = ['nomes', 'telefone','cidade']
    escrever = csv.DictWriter(arquivos_csv, fieldnames=campos, delimiter=';')
    
    escrever.writeheader()
    escrever.writerows(novo_cadastro)
print()
if apagado:
    print(f'Registro com nome {nome_para_apagar} apagado com sucesso.')
else:
    print(f'Registro com nome {nome_para_apagar} não encontrado.')
print('-'*70)