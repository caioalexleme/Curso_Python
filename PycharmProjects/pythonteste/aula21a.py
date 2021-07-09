from time import sleep


def contador(i, f, p):
    '''
    -> Faz uma contagem e mostra na tela
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    '''
    c = i
    while c <= f:
        sleep(0.3)
        print(f'{c} ', end='')
        c += p
    print('FIM!')


help(contador)
contador(0, 100, 10)
