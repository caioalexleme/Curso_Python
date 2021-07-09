from math import sin, cos, tan, radians
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo {} tem o COSSENO {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ângulo {} tem a TANGENTE {:.2f}'.format(ângulo, tangente))
