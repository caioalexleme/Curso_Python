'''from math import floor'''
from math import trunc
num = float(input('Digite um número real: '))
'''print('Você digitou {}. O número tem a parte inteira {}'.format(num, floor(num)))'''
print('Você digitou {}. O número tem a parte inteira {}'.format(num, trunc(num)))
print('Você digitou {}. O número tem a parte inteira {}'.format(num, int(num)))
