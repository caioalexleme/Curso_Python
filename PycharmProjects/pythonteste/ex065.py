n = int(input('Digite um valor: '))
soma = maior = menor = n
cont = 1
média = 0
opção = str(input('Quer continuar? [S/N] ')).strip().upper()
while opção != 'N':
    n = int(input('Digite um valor: '))
    soma += n
    cont += 1
    média = soma / cont
    opção = str(input('Quer continuar? [S/N] ')).strip().upper()
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print('Você digitou {} número(s) e a média foi {}'.format(cont, média))
print('O maior valor foi o {} e o menor foi o {}'.format(maior, menor))
