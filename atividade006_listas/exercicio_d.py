# Faça um programa que preencha uma lista com as notas de 4 alunos, depois imprima a média.
import os


os.system('cls')


soma = 0
media = []

# Entrada de dados
for i in range(1, 5):
    nota = input(f'{i}º aluno: ')
    
    soma += nota
    
print(f'{nota}')
 