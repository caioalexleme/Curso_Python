listam = list()
lista = list()
dicio = dict()
totpes = 0
totidade = 0
while True:
    dicio['nome'] = str(input('Nome: '))
    dicio['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if dicio['sexo'] == 'F':
        listam.append(dicio['nome'])
    dicio['idade'] = int(input('Idade: '))
    lista.append(dicio.copy())
    totpes += 1
    totidade += dicio['idade']
    media = totidade / totpes
    dicio = dict()
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if opc == 'N':
        break
print('-=' * 30)
print(lista)
print(f'    - O grupo tem {totpes} pessoas.')
print(f'    - A média de idade é de {media} anos.')
print(f'    - As mulheres encontradas foram: {listam}')
