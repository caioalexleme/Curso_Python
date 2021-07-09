jogador = dict()
partidas = []
totgols = 0
jogador['nome'] = str(input('Nome do jogador: '))
npartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for cont in range(0, npartidas):
    c = int(input(f'Quantos gols na {cont + 1}ª partida? '))
    partidas.append(c)
    totgols += c
jogador['gols'] = partidas
jogador['total'] = totgols
print(f'{"-=" * 30}\n{jogador}\n{"-=" * 30}')
for chave, valor in jogador.items():
    print(f'O campo {chave} tem o valor {valor}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {npartidas} partidas.')
for c in range(0, npartidas):
    print(f'    => Na {c+1}ª partida fez {partidas[c]} gol(s)!')
print('Foi um total de {} gol(s).'.format(jogador['total']))
