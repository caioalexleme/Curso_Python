c = soma = cont = 0
while c != 999:
    n = int(input('Digite um número [999 para parar]: '))
    soma += n
    c = n
    cont += 1
print('Você digitou {} números'.format(cont - 1))
print('A soma dos números digitados é igual a {}'.format(soma - 999))
