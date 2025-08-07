import random
n = ['0', '1', '2', '3', '4', '5']
pc = random.choice(n)
v = str(input('Digite um numero de 0 a 5: '))
if v == pc:
    print('Parabens Você acertou!!')
else:
    print('Quaseeee!!')
print('O numero da Maquina {} e o seu digito foi {}'.format(pc, v))