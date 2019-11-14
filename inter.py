class Calculadora():

    num = print('''Selecione qual base deseja utilizar para fazer os calculos:
     1- Binário
     2- Hexadecimal''')
    opção = int(input('Base escolhida: '))
    if opção ==1:
        print('Opção escolhida: {}'.format(opção))
    elif opção ==2:
        print('Opção escolhida: {}'.format(opção))
    else:
        print('Opção inválida')

    op = print('''Selecione qual operação deseja realizar:
    1- Soma
    2- Subtração''')
    esc = int(input('Operação escolhida: '))
    if esc == 1:
        print('Operação escolhida: ', esc)
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        soma = n1 + n2
        print('Soma = {}'.format(soma, bin(soma)[2:]))
    elif esc == 2:
        print('Operação escolhida: {}' .format(esc))
        print('Operação escolhida: ', esc)
        n1 = input('Digite o primeiro valor: ')
        n2 = input('Digite o segundo valor: ')
        sub = n1 - n2
        print('Subtração = {}'.format(sub, bin(sub)[2:]))
    else:
        print('Operação inválida')


class Conversão():

    num = int(input('Digite um número: '))
    print('''Escolha uma das opções abaixo:
    1- Converter para binário
    2- Converter para octal
    3- Converter para hexadecimal''')

    opção = int(input('Opção escolhida: '))
    if opção == 1:
        print('{} convertido para binário é igual a {}' .format(num, bin(num)[2:]))
    elif opção == 2:
        print('{} convertido para octal é igual a {}' . format(num, oct(num)[2:]))
    elif opção == 3:
        print('{} convertido para hexadecimal é igual a {}' .format(num, hex(num)[2:]))
    else:
         print('opção inválida')

