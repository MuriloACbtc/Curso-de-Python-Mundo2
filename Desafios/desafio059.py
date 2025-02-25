

print('CALCULADORA')

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
print('''Digite
[ 1 ] Para SOMAR
[ 2 ] Para MULTIPLICAR
[ 3 ] Para ver qual é MAIOR
[ 4 ] Para ter NOVOS NÚMEROS
[ 5 ] Para SAIR do programa''')
acao = int(input('Digite aqui a sua escolha: '))

while acao != 5:
    if acao == 1:
        print('A SOMA de {} e {} resulta em {}.'.format(n1, n2, n1 + n2))
        print(' ====================')
        acao = int(input('Digite aqui sua NOVA escolha: '))

    elif acao == 2:
        print('A MULTIPLICAÇÃO de {} e {} resulta em {}.'.format(n1, n2, n1 * n2))
        print(' ====================')
        acao = int(input('Digite aqui sua NOVA escolha: '))

    elif acao == 3:
        if n1 > n2:
            print('O MAIOR número é o {}, e o menor é o {}.'.format(n1, n2))
        else:
            print('O MAIOR número é o {} e o menor é o {}.'.format(n2, n1))
        print(' ====================')
        acao = int(input('Digte aqui sua NOVA escolha: '))

    elif acao == 4:
        n1 = float(input('Digite o NOVO primeiro número: '))
        n2 = float(input('Digite o NOVO segundo número: '))
        print(' ====================')
        acao = int(input('Digte aqui sua NOVA escolha: '))
    else:
        print('Você digitou errado')
        acao = int(input('Digte aqui novmente sua NOVA escolha: '))

print('Você SAIU do programa.')
