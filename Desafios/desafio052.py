
n = int(input('Digite um número: '))
a = 'é primo'
for c in range(2, n):
    if n % c == 0:
        a = 'não é primo'
print('O número {} {}'.format(n, a))
