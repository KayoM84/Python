n = int(input('Digite o primeiro Numero: '))
n2 = int(input('Digite o segundo Numero: '))
n3 = int(input('Digite o Terciero Numero: '))

if n < n2 and n < n3:
    print('O numero {} é Menor que {} e {}'.format(n, n2, n3))
elif n > n2 and n > n3:
    print('O numero {} é Maior que {} e {}'.format(n, n2, n3))

    
elif n2 < n and n2 < n3:
    print('O numero {} é Menor que {} e {}'.format(n2, n, n3))
elif n2 > n and n2 > n3:
    print('O numero {} é Menor que {} e {}'.format(n2, n, n3)) 


elif n3 < n and n3 < n2:
    print('O numero {} é Menor que {} e {}'.format(n3, n, n2))
elif n2 > n and n2 > n3:
    print('O numero {} é Menor que {} e {}'.format(n2, n, n3))
    
print('Ate mais!')