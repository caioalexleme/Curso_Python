from random import randint
computador = randint(0, 10)
jogador = int(input('Em que número pensei (entre 0 e 10): '))
erro = 0
while computador != jogador:
    erro += 1
    if jogador < computador:
        jogador = int(input('É um número maior, tente novamente: '))
    else:
        jogador = int(input('É um número menor, tente novamente: '))
print('Venceu, joguei no {}, mas você errou {} vez(es)!'.format(computador, erro))
