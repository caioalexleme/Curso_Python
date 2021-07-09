valores = list()
while True:
    n = (int(input('Digite um valor: ')))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if opção == 'N':
        break
valores.sort()
print('-=' * 30)
print(f'Você digitou os valores: {valores}')
