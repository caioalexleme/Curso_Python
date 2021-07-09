peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / altura ** 2
print('Seu IMC: {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc <= 25:
    print('Seu peso é ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <=40:
    print('Obeso(a)')
else:
    print('Obesidade mórbida.')
