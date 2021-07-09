sal = float(input('Digite o valor do seu salário: R$'))
if(sal > 1250):
    print('Seu salário agora é R${:.2f}'.format(sal + (sal * 0.10)))
else:
    print('Seu salário agora é R${:.2f}'.format(sal + (sal * 0.15)))
