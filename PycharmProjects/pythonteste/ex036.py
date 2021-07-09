print('-=-' * 10, '\nEmpréstimo Garantido!!!')
print('-=-' * 10)
valor = float(input('Qual o valor da casa: R$'))
sal = float(input('Qual seu salário? R$'))
anos = int(input('Pretende pagar em quantos anos? '))
meses = anos * 12
prest = valor / meses
if prest > (sal*0.30):
    print('Empréstimo não autorizado as prestações de R${:.2f} são mais que 30% do seu salário!'.format(prest))
else:
    print('Empréstimo autorizado, com pretações de R${:.2f}!'.format(prest))
