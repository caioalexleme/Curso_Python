def teste(b):
    global a   # Transforma a variável global fora da função '5' no valor '8' definido abaixo local
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')
