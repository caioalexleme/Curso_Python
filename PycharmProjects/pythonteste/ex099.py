lista = list()


def maior(*num):
    for valor in num:
        print(f'{valor} ')


while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opc == 'N':
        break
print(lista)
maior(lista)
lista.sort()
print(f'O maior valor é {lista[-1]}')
