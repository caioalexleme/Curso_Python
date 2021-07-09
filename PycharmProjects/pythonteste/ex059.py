from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Qual é o maior
    [ 4 ] Digitar novos números
    [ 5 ] Sair do programa''')
    opção = int(input('>>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('-=-' * 15)
        print('A soma dos valores é {}'.format(soma))
        print('-=-' * 15)
    elif opção == 2:
        mult = n1 * n2
        print('-=-' * 15)
        print('A multiplicação entre os valores é {}'.format(mult))
        print('-=-' * 15)
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('-=-' * 15)
        print('O maior valor é o ({})'.format(maior))
        print('-=-' * 15)
    elif opção == 4:
        print('-=-' * 15)
        n1 = int(input('Digite um novo valor: '))
        n2 = int(input('Digite outro novo valor: '))
        print('-=-' * 15)
    elif opção == 5:
        print('Finalizando....')
    else:
        print('-=-' * 15)
        print('[ERRO] opção inválida! TENTE NOVAMENTE!')
        print('-=-' * 15)
    sleep(2)
print('Fim do programa! Volte sempre')
