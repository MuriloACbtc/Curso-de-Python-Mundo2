

n = int(input('Digite quantos números quer ver da \033[1;33mSequência de Fibonacci\033[m: '))
t1 = 0
t2 = 1
t3 = 1
contador = 2
if n == 0:
    print('Errado')
if n == 1:
    print(t1)
if n == 2:
    print('{}, {}'.format(t1, t2, end=' '))
if n == 3:
    print('{}, {}, {}'.format(t1, t2, t3))
else:
    print('{}, {},'.format(t1, t2), end=' ')
    while contador < n:
        t3 = t2 + t1
        print('{},'.format(t3), end=' ')
        t1 = t2
        t2 = t3
        contador += 1
print('FIM')

#fiz de novo sem ver em nenhum lugar:
'''
n = int(input('Digite quantos números você quer ver da sequêmcia de fibonacci: '))
n1 = 0
n2 = 1
n3 = 1
if n == 0:
    print('Errou, digite certo!')
elif n == 1:
    print('{}, FIM'.format(n1))
elif n == 2:
    print('{}, {}, FIM'.format(n1, n2))
elif n == 3:
    print('{}, {}, {}, FIM'.format(n1, n2, n3))
else:
    print('{}, {},'.format(n1, n2), end=' ')
    c = 2
    while c < n:
        n3 = n2 + n1
        print('{},'.format(n3), end=' ')
        n1 = n2
        n2 = n3
        c += 1
print('FIM')
'''