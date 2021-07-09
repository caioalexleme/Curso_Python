while True:
    n = float(input('Quer ver a tabuada de qual valor? '))
    print('-' * 35)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n:.0f} x {c:2} = {n * c:.0f}')
    print('-' * 35)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
