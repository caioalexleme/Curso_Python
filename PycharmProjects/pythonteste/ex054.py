from datetime import date
atual = date.today().year
maioridade = 0
menoridade = 0
for nascimento in range(1, 8):
    data = int(input('Em que ano a {}ª pessoa nasceu? '.format(nascimento)))
    idade = atual - data
    if idade >= 21:
        maioridade += 1
    else:
        menoridade += 1
print('{} pessoa(s) ja atingiram a maioridade!'.format(maioridade))
print('{} pessoa(s) não atingiram a maioridade!'.format(menoridade))
