v = float(input('Digite a Velocidade de seu Carro -> '))
if v <= 80.00:
    print('Parabens voce esta no limite!')  
elif v >= 80.00:
    multa = (v - 80)*7
    print('Sua multa ficou no valor de R${:.2f}'.format(multa))
else:
    print('Voce foi multado em 7 reais!')
print("Sua KM foi {}KM".format(v))