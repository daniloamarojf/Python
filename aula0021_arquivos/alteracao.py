import os
import csv


os.system('cls')

arquivo = 'arquivos_csv/gravacao/alunas.csv' # caminho do arquivo
nome_para_alterar = input('Digite o nome que deseja alterar: ') # Escolhendo o nome que deseja alterr dados
novo_telefone = input('Digite novo telefone: ') # Entardo con novo telefone

# novo_cadastro = [] # Lista para receber cadastro atualizado
alterado = False 

# Lendo do dados do arquivo
with open(arquivo, 'r') as arquivo_csv:
    leitura = csv.DictReader(arquivo_csv, delimiter=';') # lê csv e intepreta como dicionário
    cadastro = list(leitura) # Convertendo o dicionário em uma lista

    
for registro in cadastro: # para cada registro dentro do cadastro
    if registro['nome'] == nome_para_alterar: # se nome igual o nome declarado
        registro['telefone'] = novo_telefone # telefone recebe o novo telefone
    alterado = True    # confirmando alteração
# novo_cadastro.append(registro)       

# Reescrevendo o arquivo com alteração
with open(arquivo, 'w', newline='') as arquivo_csv:
                        # newline='': Evita  a adição de linhas em branco extras 
                        # ao gravar o arquivo em algumas plataformas.
    campos = ['nome', 'telefone','cidade']
    escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')
                                    
    escrever.writeheader()
    escrever.writerows(cadastro)

print() 
if alterado:
    print(f'Registro com o nome {nome_para_alterar} foi alterado.')
else:
    print(f'Registro com o nome {nome_para_alterar} não encontrado.')
