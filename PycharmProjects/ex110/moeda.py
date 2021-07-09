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


def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-' * 30)
