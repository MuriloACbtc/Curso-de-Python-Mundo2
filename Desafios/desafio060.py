
n = int(input('Digite um \033[34mnúmero\033[m inteiro para ver seu \033[33mfatorial\033[m: '))
f = n
print(f'\033[1m{n}!\033[m =', end=' ')
while n > 1:
    print(n, end=' x ')
    f = f * (n-1)
    n = n - 1
print('1 =', f)
