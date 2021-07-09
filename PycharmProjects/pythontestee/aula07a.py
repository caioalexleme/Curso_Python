nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))
n1 = int(input('Digite um número: '))
n2 = int (input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}!'.format(n1+n2), end=' ') #(end) Mantém esse e o próximo print na mesma linha
print('A soma é {}. O produto é {}. A divisão é {:.3f}.'.format(s, m, d)) #Limitando o res da divisão em três casas decimais.(f=flutuandte)
print('A divisão inteira é {}.\n A potência é {}'.format(di, e)) #(\n) Quebra a linha
