valores = []
maior = menor = 0
for cont in (range(0, 5)):
    valores.append(int(input(f'Digite um valor na posição {cont}: ')))
    if cont == 0:
        maior = menor = valores[0]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print(f'{"=-" * 40}\nVocê digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {min(valores)} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
