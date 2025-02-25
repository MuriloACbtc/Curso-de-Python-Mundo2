

print('Escreva dois números \033[1;33minteiros\033[m')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O primeiro número é maior, pois {} é maior que {}'.format(n1, n2))
elif n2 > n1:
    print('O segundo número é maior, pois {} é maior que {}'.format(n2, n1))
else:
    print('Os dois números são iguais! \n{} e {}'.format(n1, n2))
