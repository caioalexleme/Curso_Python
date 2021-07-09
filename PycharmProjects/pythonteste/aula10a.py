n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Sua média foi {:.1f}'.format(m))
if m >= 6:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

print('Sua média foi boa! PARABÈNS!' if m >= 6 else 'Sua média foi ruim! ESTUDE MAIS')
#Condição simplificada ^
