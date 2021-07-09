termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
c = 0
while c <= 9:
    c += 1
    print('{}'.format(termo), end=' → ')
    termo += razão
print('ACABOU')