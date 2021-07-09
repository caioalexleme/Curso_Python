from datetime import date
pessoa = dict()
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['idade'] = date.today().year - int(input('Ano de nascimento: '))
    pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
    if pessoa['ctps'] == 0:
        break
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário R$'))
    pessoa['aposentadoria'] = (pessoa['contratação'] + 35) - date.today().year + pessoa['idade']
    break
print('=-' * 20)
for k, v in pessoa.items():
    print(f'  - {k} tem o valor {v}')
