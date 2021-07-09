n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
     'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    número = int(input('Digite um número entre 0 e 20: '))
    while número < 0 or número > 20:
        número = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {n[número]}')
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opção == 'N':
        print(f"{'-' * 40}\n{'Volte sempre':^40}")
        break
