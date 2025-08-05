nome = input('Digite o seu Nome: ').strip()
nome = nome.lower()
vf = nome[:5] == 'santo' in nome
print('Sua cidade tem Santo? {}'.format(vf))
print('Sua cidade é:{} '.format(nome.upper()))