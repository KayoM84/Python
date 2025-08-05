import math
co = float(input('Comprimento do cateo oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa var medir {:.2f}'.format(hi))