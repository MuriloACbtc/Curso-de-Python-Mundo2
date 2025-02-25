
n = float(input('Digite um número (999 para parar): '))
s = 0
nn = 0
while n != 999:
    s = s + n
    nn = nn + 1
    n = float(input('Digite um número: '))
print('Você parou.\nVocê digitou {} números.\nE a soma de todos eles da {}.'.format(nn, s))
