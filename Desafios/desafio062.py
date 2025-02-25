
n = float(input('Digite o \033[34mprimeiro termo\033[m da \033[1;34mPA\033[m: '))
r = float(input('Digite a \033[34mrazão\033[m da \033[1;34mPA\033[m: '))
z = n
print('Os 10 primeiros termos da PA: ', end=' ')
while n < z + (r*10):
    print(n, end=' ')
    n = n + r

escolha = int(input('''Digite 
[ 1 ] para escolher quantos termos você quer que mostre ainda, e 
[ 2 ] para mostrar 0 termos.
Digite sua escolha: '''))

while escolha == 1:
    e = int(input('Digite quantos termos ainda quer ver: '))
    c = 0
    while c < e:
        print(n, end=' ')
        n = n + r
        c += 1

    escolha = int(input('''Digite 
    [ 1 ] para escolher quantos termos você quer que mostre ainda, e 
    [ 2 ] para mostrar 0 termos.
    Digite sua escolha: '''))

print('Acabou-se')
