l = int(input('Digite sua largura de Parede: '))
a = int(input('Digite Altura da Parede: '))
t = int(input('Digite a Quantidade de Tinta em Litros: '))
r1 = l * 2
r2 = a * 2
r3 = r1 + r2
r4 = t ** 2
f = r3 - r4
print('Parede:{} metro totais'.format(r3))
print('Tinta em metros Quadrado:{}'.format(r4))