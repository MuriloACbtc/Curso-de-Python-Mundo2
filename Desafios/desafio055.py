
maiorp = 0
menorp = 0
for c in range(1, 6):
    peso = float(input('Digite o pesso da {}ª pessoa: '.format(c)))
    if c == 1:
        maiorp = peso
        menorp = peso
    else:
        if peso > maiorp:
            maiorp = peso
        if peso < menorp:
            menorp = peso
print('O maior peso foi de {}Kg'.format(maiorp))
print('O menor peso foi de {}Kg'.format(menorp))
