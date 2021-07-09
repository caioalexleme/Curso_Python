from datetime import date


def voto(y):
    idade = date.today().year - nasc
    if idade < 16:
        print(f'Com {idade} anos: Não pode votar')
    elif idade < 18 or idade >= 65:
        print(f'Com {idade} anos: Voto opcional')
    else:
        print(f'Com {idade} anos: Voto obrigatório')


nasc = int(input('Qual o ano do seu nascimento? '))
voto(nasc)
