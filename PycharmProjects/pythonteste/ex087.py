matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = s3 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if l == 1:
            if matriz[l][c] > maior:
                maior = matriz[l][c]
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            s3 += matriz[l][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {s3}.')
print(f'O maior valor da segunda linha é {maior}.')
