aluno = dict()
aluno['nome'] = str(input('Nome: ')).strip()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print(f'Média é igual a {aluno["media"]}')
if aluno['media'] < 7:
    print('Situação é igual a Reprovado!')
else:
    print('Situação é igual a Aprovado!')
