def metade(num=0):
    res = num / 2
    return res


def dobro(num=0):
    res = num * 2
    return res


def aumentar(num=0, taxa=0):
    res = num + (num * taxa / 100)
    return res


def diminuir(num=0, taxa=0):
    res = num - (num * taxa / 100)
    return res


def moeda(preço=0, moeda='RS'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
