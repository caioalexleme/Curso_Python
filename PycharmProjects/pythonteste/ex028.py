import random
n1 = 0
n2 = 1
n3 = 2
n4 = 3
n5 = 4
n6 = 5
lista = [n1, n2,  n3, n4, n5, n6]
escolhido = random.choice(lista)
acerto = int(input('Digite um número de 0 à 5 e veja se você acertou: '))
print('O número escolhido foi {}'.format(escolhido))
if(acerto == escolhido):
    print('Você acertou, PARABÈNS!')
else:
    print('Você errou, TENTE NOVAMENTE!')
