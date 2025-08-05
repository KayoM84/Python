# count = conta letras na frase
# upper = deixa a letra em maiusculo
# len = conta as letras da frase
# strip = tirar espaços indesejados -> mas so funciona no começo e no fim.  OBS:"O mesmo tem variavel 'R' de Right e 'L' left a Esquerda"
# in = consulta se tem o mesmo no exemplo: Frase
# find = busca a palavra nas Picadas do Mesmo
# Exemplo de Find = "Curso em Video" "0'1'2'3'4'-'5'-'67'-'8'-'9'10'11'12'13'" -> ele conta os espaços 5 é espaço junto de 8
# Lower = deixa tudo minusculo
# split = dividir as palavras
# replace = Trocar letras




#frase = 'Curso em Video Python'
#print(frase[::2])
#palavra = """Oi, bom dia, meu nome é Kayo
#e estou testando Programação.
#E este é um de meus começo em 
#Python, Obrigado!                         """
#print(palavra.count('o'))
#print(frase.upper().count('O'))
#print(palavra.upper().count('O'))
#print(len(palavra))
#print(len(frase))
#print(len(palavra.strip()))
#print(palavra.replace('Python', 'Android'))

#############################################################

#Não vai funcionar, porque não salvei a alteração

#frase = 'Curso em Video Python'
#frase.replace('Python', 'Android')
#print(frase)

#Vai funcionar porque salvei a alteração

#frase = 'Curso em Video Python'
#frase = frase.replace('Python', 'Android')
#print(frase)

#So responde com True ou False

#frase = 'Curso em Video Python'
#print('Curso' in frase)

#Procura o numero do desmanbramento

frase = 'Curso em Video Python'
print(frase.find('Video'))

#No caso se colocar o 'Video' de find em 'video' minusculo não acha, mas se colocarmos o 'lower' antes ele consegue procurar
#porque todos do desmanbramento ficam minusculo

frase = 'Curso em Video Python'
#errado
print(frase.find('video'))
#certo
print(frase.lower().find('video'))
#A divisão fica aqui
print(frase.split())



#Filtro Divisão 
#frase = 'Curso em Video Python'
#dividido = frase.split()
#print(dividido[0])
#print(dividido[0] [3])