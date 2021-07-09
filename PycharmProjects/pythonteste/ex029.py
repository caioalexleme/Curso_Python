km = int(input('Você passou à quantos km/h: '))
if(km > 80 ):
    valor = (km - 80) * 7
    print('Você foi multado, o valor da multa é R${},00!'.format(valor))
else:
    print('Tranquilo, sem multas, dirija sempre com segurança!')
