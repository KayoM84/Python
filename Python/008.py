while True:
    print('Escoha uma das opções:')
    print('1 - Quilometro')
    print('2 - Metro')
    print('3 - Milimetro')
    print('4 - Sair')

    opcao = input("Digite o Numero da sua Escolha:")

    if opcao == '1':
        m = int(input('Quilometro: '))
        me = m * 1.000
        mm = m * 1000000
        print('Seu valor em metro: {}'.format(me))
        print('Seu valor em Milimetro: {}'.format(mm))
        break

    elif opcao == '2':
        m = int(input('Metro: '))
        me = m / 1000
        mm = m * 1000
        print('Seu valor em Quilometro:{}'.format(me)) 
        print('Seu valor em Milimetro:{}'.format(mm))
        break

    elif opcao == '3':
        m = int(input('Milimetro: '))
        me = m / 1000
        mm = m / 1000000
        print('Seu calor em Milimetro:{}'.format(me))
        print('Seu valor em Quilometro:{}'.format(mm)) 
        break

    elif opcao == '4':
        print('Muito Obrigado!')
        break

    else:
        print('Opção invalida. tente novamente.')