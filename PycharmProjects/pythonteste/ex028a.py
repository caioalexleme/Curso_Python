from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um nº entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÈNS! Você conseguiu me vencer!')
else:
    print('Ganhei eu pensei no número {} e não no {}!'.format(computador, jogador))
