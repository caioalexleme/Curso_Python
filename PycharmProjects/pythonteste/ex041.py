from datetime import date
ano = date.today().year
nasc = int(input('Em que ano você nasceu? '))
idade = ano - nasc
if idade <= 9:
    print('Categoria Mirim')
elif idade <= 14:
    print('Categoria Infantil')
elif idade <= 19:
    print('Categoria Junior')
elif idade <= 25:
    print('Categoria Sênior')
else:
    print('Categoria Master')
