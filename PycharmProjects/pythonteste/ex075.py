núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print('-' * 40)
print(f'Você digitou os valores {núm};')
print(f'O valor "9" apareceu {núm.count(9)} vezes;')
if 3 in núm:
    print(f'O primeiro valor "3" digitado está na {núm.index(3) + 1}ª posição;')
else:
    print('O valor "3" não foi digitado em nenhuma posição;')
print('Os valores pares digitados foram', end=' ')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')
