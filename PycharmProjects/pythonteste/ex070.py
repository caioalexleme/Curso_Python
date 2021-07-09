total = mais1000 = menor = cont = 0
produtobarato = ' '
print('-' * 40, f'\n{"LOJA SUPER BARATÃO":^40}')
print('-' * 40)
while True:
    produto = str(input('Nome do produto: ')).strip()
    preço = float(input('Preço: R$'))
    opção = ' '
    total += preço
    cont += 1
    if cont == 1:
        menor = preço
        produtobarato = produto
    else:
        if preço < menor:
            menor = preço
            produtobarato = produto
    if preço > 1000:
        mais1000 += 1
    while opção not in 'SN':
        opção = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if opção == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mais1000} produto(s) custando mais de R$1000,00')
print(f'O produto mais barato foi {produtobarato} que custa R${menor:.2f}')
