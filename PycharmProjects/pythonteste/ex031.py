km = float(input('Quantos km é sua viagem? '))
if(km <= 200):
    print('O preço da viagem é R${:.2f}'.format(km * 0.50))
else:
    print('O preço da viagem é R${:.2f}'.format(km * 0.45))
