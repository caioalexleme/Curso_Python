def ficha(nome='', gols=''):
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    if nome == '':
        nome = '<desconhecido'
        print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
    elif gols == '':
        print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
    elif nome == '' and gols == '':
        nome = '<desconhecido>'
        print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
    else:
        print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


ficha(str(input('Nome do jogador: ')), str(input('Número de gols: ')))
