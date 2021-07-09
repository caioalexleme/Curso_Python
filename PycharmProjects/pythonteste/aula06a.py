n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
#print('A soma de', n1, 'com', n2,'vale',s) #funciona porém precisa de muita vírgula e muitas aspas
print('A soma entre {} e {} é {}'.format(n1, n2, s))
print('A soma entre {0} e {1} é {2}'.format(n1, n2, s)) #Mesmo resultado, identificando a ordem dos valores
print(type(n1))

