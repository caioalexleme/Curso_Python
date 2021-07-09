n1 = float(input('Qual sua primeira nota: '))
n2 = float(input('Qual sua segunda nota: '))
média = (n1 + n2) / 2
if n1 < 0 or n1 > 10 or n2 < 0 or n2 > 10:
    print('Algum valor foi digitado errado! confira os dados e tente novamente!')
elif média < 5:
    print('Reprovado')
elif média < 7:
    print('Recuperação')
else:
    print('Aprovado')
