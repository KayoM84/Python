dias = int(input('Qunatos dias alugados? '))
km = float(input('Quantos km Rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagat é de R${:.2f}'.format(pago))