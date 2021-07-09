a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
# Verificando menor valor
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
#Verificando o maior valor
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
