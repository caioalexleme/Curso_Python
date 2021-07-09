from datetime import date
ano = int(input('Qual seu ano de nascimento? '))
alist = date.today().year
if (alist - ano) == 18:
    print('Está na hora de se alistar')
elif (alist - ano) < 18:
    print('Ainda faltam {} anos pra você se alistar'.format(18 - (alist-ano)))
elif (alist - ano) > 18:
    print('Você ja passou {} anos para fazer alistamento'.format((alist-ano) - 18))
