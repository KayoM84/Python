n1 = float(input('Digite o Preço do produto: R$ '))
n2 = 5
n3 = n2 / 100
n4 = n3 * n1
n5 = n1 - n4
print('O valor do produto é de R${} \n no temos {} de Desconto \n e com o desconto o produto fica R${:.2f}'.format(n1, n2, n5))
