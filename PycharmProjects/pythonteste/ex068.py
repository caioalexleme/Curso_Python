from random import randint
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
c = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    opção = ' '
    while opção not in 'PI':
        opção = str(input('PAR OU ÍMPAR [P/I]? ')).strip().upper()[0]
    resultado = computador + jogador
    print('-' * 40)
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {resultado}', end=' ')
    if resultado % 2 == 0:
        print('DEU PAR')
        resultado = 'PAR'
    else:
        print('DEU ÍMPAR')
        resultado = 'ÍMPAR'
    print('-' * 40)
    if opção in 'Pp':
        jogador = 'PAR'
    elif opção in 'Ii':
        jogador = 'ÍMPAR'
    if jogador == resultado:
        print('Você VENCEU!\nVamos jogar novamente')
        print('=-' * 20)
        c += 1
    else:
        print('Você perdeu')
        print('=-' * 20)
        print(f'GAME OVER! Você venceu {c} vez(es).')
        break
