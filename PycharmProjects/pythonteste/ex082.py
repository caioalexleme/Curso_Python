lista = []
listap = []
listai = []
while True:
    n = int(input('Digite um número: '))
    opção = ' '
    lista.append(n)
    if n % 2 == 0:
        listap.append(n)
    else:
        listai.append(n)
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if opção == 'N':
        break
print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de Pares é {listap}')
print(f'A lista de Ímpares é {listai}')
