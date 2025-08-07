a = float(input('Digite o valor do Primeiro lado do Triangulo: '))
b = float(input('Digite o valor do Segundo lado do Triangulo: '))
c = float(input('Digite o valor do Terceiro lado do Triangulo: '))
if a + b > c:
    print('Primeiro lado Certo')
else:
    print('Lado não condiz')
if a + c > b:
    print('Segundo lado Certo')
else:
    print('Lado não condiz')
if b + c > a:
    print('Terceiro lado Certo')
else:
    print('Lado não condiz')
print('Primeiro lado {} = Segundo lado {} = Terceiro lado {}'.format(a, b, c))