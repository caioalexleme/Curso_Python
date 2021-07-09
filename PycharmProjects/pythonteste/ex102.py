def fatorial(num=1, show=False):
    '''
    => Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor fatorial de um número (n).
    '''
    from time import sleep
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show == True:
            print(f'{c} ', end='')
            if c > 1:
                sleep(0.9)
                print('x ', end='')
            if c == 1:
                sleep(0.9)
                print('=', end='')
                sleep(0.9)
    return f


n = int(input('Digite um número: '))
print(f' {fatorial(n, True)}')
help(fatorial)
