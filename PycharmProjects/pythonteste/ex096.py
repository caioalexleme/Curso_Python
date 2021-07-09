def area(l, c):
    a = l * c
    print(f'A área de um terreno de {l} x {c} é de {a}m²')


print(f'  Controle de Terrenos\n{"-" * 15}')
area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO: (m)')))
