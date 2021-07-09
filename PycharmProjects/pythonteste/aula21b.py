def somar(a=0, b=0, c=0):
    """
    => Faz a soma de três valores e mostra o resultado na tela.
    :param a: O primeiro valor
    :param b: O segundo valor
    :param c: O terceiro valor
    :return:
    Função criada por Caio Alexandre de Sousa Leme!
    """

    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
help(somar)
somar(3, 3, 5)
somar(c=3, b=4)
