sexo = ''
while sexo != 'M' and sexo != 'F':
    p = str(input('Digite seu sexo: [M/F]: ')).strip().upper()[0]
    sexo = p
if sexo == 'M':
    print("Seu sexo é '{}' Masculino!".format(p))
else:
    print("Seu sexo é '{}' Feminino!".format(p))