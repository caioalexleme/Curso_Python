from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
ranking = list()
print(f'    Valores sorteados:')
for chave, valor in jogo.items():
    print(f'{chave} tirou no dado {valor}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 25)
print('     == Ranking dos jogadores == ')
for c, v in enumerate(ranking):
    print(f'    {c + 1}° lugar: {v[0]} com {v[1]}')
    sleep(1)
