soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
#print('A soma entre os números digitados é igual a {}'.format(soma))
print(f'A soma vale {soma}')
nome = 'José'
idade = 33
salário = 987.3
ok = 'ok'
print(f'O {nome:->20} tem {idade:-^20} anos e ganha R${salário:.2f} {ok:-<5}')
print('O %s tem %d anos'% (nome, idade)) #Python 2
