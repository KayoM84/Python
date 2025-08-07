salario = float(input('Digite seu salario R$ '))
if salario >= 1250.00:
    n1 = salario * 0.1
    n2 = salario + n1
    print('Seu salario com almento de "10%" ficou {}'.format(n2))
else:
    n1 = salario * 0.15
    n2 = salario + n1
    print('Seu salario com almento de "15%" ficou {}'.format(n2))