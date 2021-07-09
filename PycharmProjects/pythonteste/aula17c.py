a = [2, 3, 4, 7]
b = a # Cria uma sincronização da lista A com a lista B
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print('-' * 10)
b = a [:] # Agora lista B cria ua cópia da lista A utilizando fatiamento
b[2] = 6
print(f'Lista A: {a}')
print(f'Lista B: {b}')