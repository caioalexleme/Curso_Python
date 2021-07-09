valor = float(input('Qual o valor do produto? R$'))
pagamento = int(input('''Qual a forma de pagamento? 
[1]À vista (dinheiro cheque)
[2]À vista no cartão
[3]Em até 2X no cartão
[4]3X ou mais no cartão

Digite aqui a opção: '''))
if pagamento == 1:
    print('Você ganhou 10% de desconto o valor é R${:.2f}'.format(valor - (valor * 0.10)))
elif pagamento == 2:
    print('Você ganhou 5% de desconto o valor é R${:.2f}'.format(valor - (valor * 0.05)))
elif pagamento == 3:
    print('R${:.2f}'.format(valor))
elif pagamento == 4:
    print('Seu produto fica no valor de R${:.2f}'.format(valor + (valor * 0.20)))
else:
    print('[ERRO] Opção inválida. Tente novamente')
