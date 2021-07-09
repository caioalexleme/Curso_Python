times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Atlético-PR', 'Cruzeiro',
         'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco da Gama',
         'Sport Recife', 'América-MG', 'EC Vitória', 'Paraná')
print('-=' * 30)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 30)
print(f'Os cinco primeiros são: {times[:5]}')
print('-=' * 30)
print(f'Os quatro últimos são: {times[-4:]}')
print('-=' * 30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 30)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição')
