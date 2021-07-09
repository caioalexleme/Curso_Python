frase = 'Curso em Vídeo Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print('Oi')
print("""lasjnflfnjçejfqçemrqldlçqrmfqld
qjnrqklnjrqkwnrnqlkjqkn
qjrnfçqjnçrqlfmçlqrkfmlqf
lçqjnrfçlqrnfçlfnlrçfnrqçl""") #Pode ser aspas simples três vezes. imprime o texto de acordo como foi programado (digitado)
print(frase.count('o')) #Têm tres 'o' minúsculos
print(frase.count('O')) #Têm zero 'O' maiúsculos
print(frase.upper().count('O')) #Transformei a frase em maiúsculas, e contei o nº de 'O' maiúsculos
print(len(frase)) #conta o nº de caracteres
print(len(frase.strip())) #'strip' Remove espaços indesejados
print(frase.replace('Python', 'Android')) #Trocando palavra 'Python' por 'Android'
print(frase[3]) #Exibe quarto caracter que corresponde à letra 's'
print('Curso' in frase) #A palavra 'Curso' está dentro da frase? True
print('Android' in frase) #A palavra 'Android' está dentro da frase? False
print(frase.find('Curso')) #Palavra 'Curso' começa no 1° microespaço (0)
print(frase.find('curso')) #Palavra 'curso' não existe na frase = -1
print(frase.lower().find('curso')) #Agora 'curso' existe pois antes transformei toda a frase em letras minúsculas
print(frase.split()) #Criando lista, quebrando as palavras pelos espaços
dividido = frase.split()
print(dividido[0]) #Exibe o primeiro item da lista criada
print(dividido[0][2]) #Exibe a 3ª(2) letra do 1°(0) item da lista criada
print(frase.capitalize())
print(frase.title())
print(''.join(frase))
