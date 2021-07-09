mt = float(input('Quantos metros de cobre você precisa? '))
print('Certo, então são: \n{}km ou\n{}hm ou\n{}dam ou\n{:.0f}dm ou\n{:.0f}cm ou\n{:.0f}mm ou\n'.format(mt*0.001, mt*0.01, mt*0.1, mt*10, mt*100, mt*1000))
