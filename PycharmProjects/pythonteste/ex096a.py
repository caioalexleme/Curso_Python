def área(larg, comp):
    a = larg * comp
    print(f'A área de {larg}x{comp} é de {a}m²')


print(f'  Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)
