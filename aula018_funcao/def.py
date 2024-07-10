# Definindo funções

def limpa_tela():
    '''Função para limpar o terminal
    '''
    import os
    os.system('cls')
    

def soma(a,b):
    """Função para somar dois números

    Args:
        a (int): valor de a
        b (int): valor de b
    
    Retourn:
        Retorna a soma de dois números
    """    
    
    return a + b

def firula():
    print('-'*70)
    
# Programa inicial


# Chamando a função
limpa_tela()
firula()
resposta = soma(1,2)
print(f'A soma dos 2 números é: {resposta}')
firula()
print()
    
    