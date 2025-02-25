
print('\033[1;7;37mCONVERSOR\033[m')
n = int(input('Digite um número inteiro: '))
escolha = int(input('Digite 1 para converter {} para BINÁRIO,\n2 para OCTAL,\ne 3 para HEXADECIMAL: '.format(n)))
if escolha == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(escolha, bin(n)[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL é igual a {}'.format(escolha, oct(n)[2:]))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(escolha, hex(n)[2:]))
else:
    print('Escolha direito!')