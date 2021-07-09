def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')
    tam = len(num)
    print(f'Recebi os valores {num} e são {tam} números!')

contador(1, 4, 3)
contador(3, 0)
contador(9, 6, 2, 8, 10)