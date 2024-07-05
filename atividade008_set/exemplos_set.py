import os 


os.system('cls')

# Declarando meu set
meu_set = {1, 2, 3, 4, 1}
print(type(meu_set))

meu_set_2 = set([1, 2, 8, 9, 10])
print(type(meu_set_2))

# Adicionando elementos
meu_set.add(2)
print("Adição", meu_set)

# Atualizando set
meu_set.update([3, 4, 5, 6])
print("Atualição", meu_set)

# Removendo elemento
meu_set.discard(2)
print("Remoção", meu_set)

# União
print("União")
print(meu_set | meu_set_2)
print(meu_set.union(meu_set_2))

# Interseção
print("Interseção")
print(meu_set & meu_set_2)
print(meu_set.intersection(meu_set_2))

# Diferença
print("Diferença")
print(meu_set - meu_set_2)
print(meu_set.difference(meu_set_2))

# Diferença Simétrica
print("Diferença Simétrica")
print(meu_set ^ meu_set_2)
print(meu_set.symmetric_difference(meu_set_2))

