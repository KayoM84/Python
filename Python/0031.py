v = float(input('Qual a distancia de sua Viagem em KM: '))
if v <= 200.00:
    n1 = 0.50 * v
    print('Sua viagem ficou no valor de R${}'.format(n1))
else:
    n2 = 0.45 * v
    print('Sua viagem ficou no valor de R${}'.format(n2))
print('Sua viagem tem {}KMs'.format(v))