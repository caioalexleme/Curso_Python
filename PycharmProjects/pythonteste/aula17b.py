valores = []
valoress = list() # Desses dois jeitos pode criar uma lista vazia
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}..', end='') # Editando como aparece os valores adicionados à lista
for c, v in enumerate(valores): # Mostrando com 'enumerate' nº da chave e o valor
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista!')

for cont in range(0, 3): # Adicionando 4 valores a lista pelo teclado
    valoress.append(int(input('Digite um valor: ')))
for c, v in enumerate(valoress): # Mostrando com 'enumerate' nº da chave e o valor
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista!')
