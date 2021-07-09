ano = int(input('Digite um ano e veja se ele é bissexto: '))
d4 = ano / 4
if(d4 % 1):
    print('Não Bissexto')
else:
    print('Bissexto')
