num = int(input('Digite um número inteiro: '))
print('''Escolha uma das opções para conversão: 
[1]Converter para BINÁRIO
[2]Converter para OCTAL
[3]Converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual à {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual à {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual à {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida! Tente novamente!')
