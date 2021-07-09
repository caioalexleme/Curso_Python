frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
#inverso = junto[::-1]   (FUNCIONA DO MESMO JEITO SEM UTILIZAR O FOR)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('o inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada não é um PALÍNDROMO!')

'''EXEMPLOS DE FRASES QUE FORMAM PALÍNDROMO:
ana
apos a sopa
a sacada da casa
a torre da derrota
o lobo ama o bolo
anotaram a data da maratona'''
