# importar a biblioteca csv
import csv
import os


# Criando um lisa de dicionários: cada dicionpario é uma linha (registro)
lista = [
    {'nome':'Ágata', 'telefone':'(32)99196-0000', 'cidade':'Juiz de Fora'},
    {'nome':'Bia', 'telefone':'(32)99196-1111', 'cidade':'Juiz de Fora'},
    {'nome':'Coly', 'telefone':'(32)99196-2222', 'cidade':'Juiz de Fora'},
    {'nome':'Isis', 'telefone':'(32)99196-3333', 'cidade':'Juiz de Fora'},
]

# Caminho para a pasta onde o csv será salvo
pasta = 'arquivos_csv/gravacao/'

# Verificando se a pasta existe, se não, irá criá-la
os.makedirs(pasta, exist_ok=True)

# Nome para o arquivo CSV para gravar as informações
arquivo = 'arquivos_csv/gravacao/alunas.csv'

# Caminho completo para o arquivo CSV
caminho_arquivo = os.path.join(pasta, arquivo)

# Abre o arqruivo 'arquivo' no modo de escrita ('w')
# Se o arquivo não existir, ele será criado; se existir será truncado (esvaziado)
# newline='': Evita  a adição de linhas em branco extras ao gravar o arquivo em algumas plataformas.
# as arquivos_csv: Atribui o objetivo ao 'arquivo_csv' para ser usado dentro do bloco wiht.
with open(arquivo, 'w', newline='') as arquivo_csv:
    
    # campos = ['nome', 'telefone', 'cidade']: Define a lista de nomes de campos
    # (cabeçalho das colunas  do CSV).
    campos = ['nome', 'telefone', 'cidade']
    
    # writer = csv.DictWhiter(arquivo_csv, fieldnames=campos):
    # Criar um objeto DictWhiter que usará arquivo_csv para gravar os campos
    # Fieldnames define a ordem dos campos do arquivo csv.
    # delimiter= ';' : é o separador
    escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')
    
    # Writer.writeheader(): GRava a linha do cabeçalho no
    # arquivo csv usandos nomes de campos definidos em fieldnames.
    escrever.writeheader()
    
    # Writer.writerows(): GRava todas as linhas da linha n arquivo csv
    # Cada dicionário em lista se torna uma linha no arquivo. 
    escrever.writerows(lista)
    
os.system('cls')
# Exibe uma mensagem indicando que o arquivo foi gravado com sucesso
print(f'Arquivo {arquivo} gravado com sucesso!')