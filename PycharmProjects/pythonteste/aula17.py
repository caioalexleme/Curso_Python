lanche = ['Hamburguer', 'Suco', 'Pizza', 'Pudim']
print(lanche)
lanche.append('Cookie') # Insere um item à lista na última posição
print(lanche)
lanche.insert(0, 'Hot-Dog') # Insere um item à lista em qualquer posição
print(lanche)
del lanche[3] # Apaga um item da lista
print(lanche)
lanche.pop() # apaga o ultimo item da lista
print(lanche)
lanche.pop(2) # Também apaga um item da lista utilizando parâmetro
print(lanche)
lanche.remove('Hamburguer') # Apaga um item da lista utilizando o valor
print(lanche)
valores = list(range(4, 11)) # Criando uma lista usando 'list' e o 'range'
print(valores)
valoress = [8, 2, 5, 4, 9, 3, 0]
print(valoress)
valoress.sort() # Ordena os valores da lista
print(valoress)
valoress.sort(reverse=True) # Ordena os valores na ordem reversa
print(valoress)
print(len(valoress)) # Indica o número de índices da lista
