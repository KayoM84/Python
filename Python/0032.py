ano = int(input('Digite um Ano: '))
if (ano / 4) % 2 == 0:
    print('{} É um ano Bissexto'.format(ano))
    print('Seu Ano tem 366 Dias')
else:
    print('Seu Ano não é um Ano Bissexto')
    print('Seu Ano tem 355 Dias')