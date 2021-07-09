nome = str(input('Nome completo: ')).strip()
print(nome)
print(nome.upper())
print(nome.lower())
dividido = nome.split()
print('O nome tem {} caracteres sem contar os espaços ok?'.format(len(nome) - nome.count(' ')))
print('O primeiro nome tem {} letras'.format(len(nome.split()[0])))

