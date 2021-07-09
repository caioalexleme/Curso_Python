import emoji
from math import sqrt, floor, ceil
num = float(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrada de {} é igual à {}\nArredondando para baixo fica {}\nArredondando para cima fica {}'.format(num, raiz, floor(raiz), ceil(raiz)))
print(emoji.emojize(':sunglasses:, :cupid:', use_aliases=True))
