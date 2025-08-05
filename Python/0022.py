nome = input('Digite seu Nome Completo: ').strip()
print('Seu nome em Caixa Alta:{}'.format(nome.upper()))
print('Seu nome em Letra Minuscula:{}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) -nome.count('a') -nome.count(' ')))
