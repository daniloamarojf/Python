import os


class Pessoa:
    def __init__(self, nome, cpf, nascimento, cep, cidade, estado):
        # inicializando os atributos
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.cep = cep
        self.cidade = cidade
        self.estado = estado
        
        
# Solicitando entrada de dados ao usuário
os.system
print('-'*70)
nome = input('Digite o nome: ')
cpf = input('Digite o CPF: ')
nascimento = input('Digite o ano de nascimento: ')
cep = input('Digite o CEP: ')
cidade = input('Digite a cidade: ')
estado = input('Digite o estado: ')

# Criando um objeto da classe Pessoa com os dados fornecidos pelo usuário
pessoa1 = Pessoa(nome, cpf, nascimento, cep, cidade, estado)

# Acessando e imprimindo atributos do objeto
print('-'*70)
print('\nInformações da Pessoa:')
print('='*70)
print(f'Nome: {pessoa1.nome}')
print(f'CPF: {pessoa1.cpf}')
print(f'Ano de Nascimento: {pessoa1.nascimento}')
print(f'CEP: {pessoa1.cep}')
print(f'Cidade: {pessoa1.cidade}')
print(f'Estado: {estado}')
print('-'*70)


        