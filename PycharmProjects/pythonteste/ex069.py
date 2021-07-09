cadastro = 'CADASTRE UMA PESSOA'
maioridade = homens = mulheres = 0
while True:
    print('-' * 40)
    print(f'{cadastro:>28}')
    print('-' * 40)
    idade = int(input('Idade: '))
    sexo = ' '
    if idade > 18:
        maioridade += 1
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade < 20:
            mulheres += 1
    print('-' * 40)
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opção == 'N':
        print('=' * 5, 'FIM DO PROGRAMA' , '=' * 5)
        break
print(f'Total de pessoas com mais de 18 anos: {maioridade}.')
print(f'Ao todo temos {homens} homen(s) cadastrados.')
print(f'E, temos {mulheres} mulhere(s) com menos de 20 anos.')
