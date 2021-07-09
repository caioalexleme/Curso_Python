for c in range(0, 2):
    n = int(input('Digite um valor: '))
print('Fim')
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n      # s += n (Mesmo resultado)
print('O somatório de todos os valores foi {}'.format(s))
