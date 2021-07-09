from datetime import date
print(f'{"-" * 80}\n{"SUPERMERCADOS NOW":^80}\n{"-" * 80}')
data = date.today().strftime('%d/%m/%Y')
produtos = dict()
total = list()
vencidos = list()
while True:
    produtos['nome'] = str(input('Nome do produto: ')).strip()
    produtos['mes'] = int(input('Mês de vencimento: '))
    produtos['ano'] = int(input('Ano de vencimento: '))
    if produtos['mes'] <= date.today().month and produtos['ano'] <= date.today().year:
        produtos['vencido'] = 'Venceu'
        vencidos.append(produtos['nome'])
    total.append(produtos.copy())
    produtos.clear()
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    print('-' * 40)
    if opção == 'N':
        break
print(f'Os produtos que estão perto de vencer: {vencidos}')
print('-=' * 40)
print('Fim do programa!')