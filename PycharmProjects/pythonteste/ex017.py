import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
'''hi = (co ** 2 + ca ** 2) **(1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''  '''Usando matematicamente sem precisar importar'''
