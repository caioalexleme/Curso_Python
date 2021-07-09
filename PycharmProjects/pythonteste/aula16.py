#(TUPLA)
#[LISTA]
#{DICIONÁRIO}
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
#Na Tupla não precisa usar parenteses(), Resultado é o mesmo.
print(lanche)
print(sorted(lanche)) #Lanche ordenado
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(lanche[:-2])
print(len(lanche))
# Tuplas são imutáveis
for comida in lanche:
    print(f'Eu vou comer {comida}')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
#Mesmo resultado de cima, usando 'len' de lanche
for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]}')
print('Comi pra caramba')
for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]} na posição {c}')
