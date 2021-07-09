núm = [[], []]
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-=' * 30)
núm[0].sort()
núm[1].sort()
print(núm)
print(f'Os valores pares digitados foram: {núm[0]}')
print(f'Os valores ímparess digitados foram: {núm[1]}')
