n = float(input('Quer ver a tabuada de qual valor? '))
c = 1
print('-' * 35)
while n >= 0:
    while True:
        print(f'{n:.0f} x {c:2} = {n * c:.0f}')
        c += 1
        if c == 11:
            break
    print('-' * 35)
    c = 1
    n = float(input('Quer ver a tabuada de qual valor? '))
    print('-' * 35)
    if c == 11:
        break
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
