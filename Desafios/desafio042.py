print('\033[1;4;35m=-\033[36m=-\033[m'*16)
print('\033[1;40;7mDIGITE O TAMANHO DE 3 RETAS E VEJA SE ELAS FORMAM UM TRIÂNGULO\033[m')
print('\033[1;4;36m-=\033[35m-=\033[m'*16)
a = float(input('Reta 1: '))
b = float(input('Reta 2: '))
c = float(input('Reta 3: '))
if a+b > c and b+c > a and a+c > b:
    print('\033[32mÉ POSSIVEL\033[m formar um triângulo com as retas de tamanho {}, {} e {}!'.format(a, b, c))
    if a == b == c:
        print('Esse triângulo tem \033[33mTODOS OS LADOS IGUAIS\033[m, ou seja, ele é \033[33mEQUILÁTERO\033[m')
    elif a == b or b == c or c == a:
        print('Esse triângulo tem \033[34mAPENAS DOIS LADOS IGUAIS\033[m, ou seja, ele é \033[34mISÓSCELES\033[m')
    else:
        print('Esse triângulo tem \033[31mTODOS OS LADOS DIFERENTES\033[m, ou seja, ele é \033[31mESCALENO\033[m')

else:
    print('\033[31mNÃO É POSSIVEL\033[m formar um triângulo com as retas de tamanho {}, {} e {}!'.format(a, b, c))
