todos = []
par = []
impar = []
for n in range(0, 7):
    núm = (int(input('Digite um número: ')))
    if núm % 2 == 0:
        par.append(núm)
    else:
        impar.append(núm)
par.sort()
impar.sort()
todos.append(par[:])
todos.append(impar[:])
print('-=' * 30)
print(todos)
print(f'Os valores pares digitados foram: {par}')
print(f'Os valores ímparess digitados foram: {impar}')
