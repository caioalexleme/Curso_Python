km = float(input('Quantos km rodados: '))
dias = int(input('Quantos dias você ficou com o carro? '))
preco = (km * 0.15) + (dias * 60)
print('Você rodou {}km e ficou com o carro por {} dias, terá que pagar R${:.2f}'.format(km, dias, preco))
