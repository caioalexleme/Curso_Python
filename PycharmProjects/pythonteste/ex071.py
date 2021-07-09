print(f'{"=" * 40}\n{"BANCO CAIO":^40}\n{"=" * 40}')
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédula(s) de R${céd},00 ')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print(f'{"=" * 40}\n{"Volte sempre ao BANCO CAIO":^40}')