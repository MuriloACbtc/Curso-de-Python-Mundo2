
z = float(input('Digite o \033[1;34mprimeiro termo\033[m da PA: '))
r = int(input('Digite a \033[1;34mrazão\033[m da PA: '))
n = z
while z + (10*r) > n:
    print(n, end=' ')
    n = n + r

