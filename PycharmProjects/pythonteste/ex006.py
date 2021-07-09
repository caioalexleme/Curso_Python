num = float(input('Digite um número: '))
print('O dobro de {} é: {}.\nO triplo é: {}.\nA raiz quadrada é: {:.2f}'.format(num, num*2, num*3, num**(1/2)))
print('A raiz quadrada de {} é {:.2f}'.format(num, pow(num, (1/2))))
