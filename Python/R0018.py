import math
angulo = float('Digite o angulo que voce deseja: ')
seno = math.sin(math.radians(angulo))
print('O angulo de {} te mo seno de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo de {} tem o cossenode {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radianian(angulo))
print('O angulo de {} tem a tangente de {:.2f}'.format(angulo, tangente))