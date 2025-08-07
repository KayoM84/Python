n1 = float(input('Digite a Sua Primeira Nota: '))
n2 = float(input('Digite sua Segunda Nota: '))
m = (n1 + n2)/2
if m >= 6:
    print('Voce esta na Media, Parabens!!')
else:
    print('Infelizmente vc esta de Recuperação!')
    
print('A sua Media foi {:.1f}'.format(m))
