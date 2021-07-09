sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf': #Não precisa por 'm' e 'f' minusculos, pois o upper ja converteu, pode até tirar, funciona do mesmo jeito
    sexo = str(input('Dados inválidos, por favor informe seu sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
