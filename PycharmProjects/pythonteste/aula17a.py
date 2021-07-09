núm = [2, 5, 9, 1]
print(núm)
núm[2] = 3
print(núm)
núm.append(7)
print(núm)
núm.sort() # ordena os valores
print(núm)
núm.sort(reverse=True) # ordena os valores de modo reverso
print(núm)
print(f'Essa lista tem {len(núm)} elementos.')
núm.insert(2, 0)
print(núm)
núm.pop()
print(núm)
núm.pop(2)
print(núm)
núm.insert(2, 7)
print(núm)
núm.remove(7)
print(núm)
if 4 in núm:
    núm.remove(4)
else:
    print('Não achei o número "4"')
