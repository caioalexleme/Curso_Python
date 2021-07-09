lista = []
while True:
    n = int(input('Digite um número: '))
    opção = ' '
    lista.append(n)
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if opção == 'N':
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista, está na posição {lista.index(5)}!')
else:
    print(f'O valor 5 não foi encontrado na lista!')
