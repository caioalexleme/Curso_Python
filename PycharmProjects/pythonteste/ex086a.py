matriz = [[], [], []]
cont = 0
lista = 0
while True:
    while lista != 3:
        n = int(input(f'Digite um valor para a matriz [{cont}, {lista}]: '))
        matriz[0].append(n)
        lista += 1
    lista = 0
    cont += 1
    while lista != 3:
        n = int(input(f'Digite um valor para a matriz [{cont}, {lista}]: '))
        matriz[1].append(n)
        lista += 1
    lista = 0
    cont += 1
    while lista != 3:
        n = int(input(f'Digite um valor para a matriz [{cont}, {lista}]: '))
        matriz[2].append(n)
        lista += 1
    break
print('-=' * 30)
print(f'[ {matriz[0][0]} ]', end='')
print(f'[ {matriz[0][1]} ]', end='')
print(f'[ {matriz[0][2]} ]', end='')
print()
print(f'[ {matriz[1][0]} ]', end='')
print(f'[ {matriz[1][1]} ]', end='')
print(f'[ {matriz[1][2]} ]', end='')
print()
print(f'[ {matriz[2][0]} ]', end='')
print(f'[ {matriz[2][1]} ]', end='')
print(f'[ {matriz[2][2]} ]', end='')
