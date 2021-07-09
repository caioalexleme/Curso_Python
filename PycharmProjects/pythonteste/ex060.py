n1 = int(input('Digite um número e descubra seu fatorial: '))
c = n1
while c != 1:
    n1 = n1 * (c-1)
    c -= 1
print(n1)
