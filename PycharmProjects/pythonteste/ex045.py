from random import randint
from time import sleep
print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
computador = randint(0, 2)
você = int(input('Qual é a sua jogada? '))
pedra = 0
papel = 1
tesoura = 2
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-' * 20)
if computador == pedra:
    print('Computador jogou Pedra')
elif computador == papel:
    print('Computador jogou Papel')
elif computador == tesoura:
    print('Computador jogou Tesoura')
if você == pedra:
    print('Jogador jogou Pedra')
elif você == papel:
    print('Jogador jogou Papel')
elif você == tesoura:
    print('Jogador jogou Tesoura')
else:
    print('Jogador digitou errado, Tente novamente')
print('-=-' * 20)
if computador == você:
    print('Empate, Tente novamente!')
if computador == pedra and você == papel:
    print('Jogador vence')
elif computador == pedra and você == tesoura:
    print('Computador vence')
elif computador == tesoura and você == papel:
    print('Computador vence')
elif computador == tesoura and você == pedra:
    print('Jogador vence')
elif computador == papel and você == tesoura:
    print('Jogador vence')
elif computador == papel and você == pedra:
    print('Computador vence')
