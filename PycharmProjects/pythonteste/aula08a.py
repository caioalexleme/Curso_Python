import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual à {}\nArredondando para cima fica {}\nArredondando para baixo fica {}'.format(num, raiz, math.ceil(raiz), math.floor(raiz)))
