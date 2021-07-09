def metade(num=0, formato=False):
    res = num / 2
    return res if formato is False else moeda(res)


def dobro(num=0, formato=False):
    res = num * 2
    return res if not formato else moeda(res) # Mesma funcionalidade do 'return' acima


def aumentar(num=0, taxa=0, formato=False):
    res = num + (num * taxa / 100)
    return res if not formato else moeda(res)


def diminuir(num=0, taxa=0, formato=False):
    res = num - (num * taxa / 100)
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='RS'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
