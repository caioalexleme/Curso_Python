print('=' * 40)
print('{:^40}'.format('10 TERMOS DE UMA PA'))
print('=' * 40)
for c in range(0, 1):
    termo = int(input('Primeiro termo: '))
    razão = int(input('Razâo: '))
    for cont in range(0, 10):
        print(termo, end=' → ')
        termo += razão
print('ACABOU')
