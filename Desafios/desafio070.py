
print('{:-^40}'.format(' LOJÃO '))
print(f'{' COMPRAS ':=^40}')

maisdemil = 0
prod = str(input('Digite o nome do produto: ')).strip()
prodmaisbarato = prod
preco = float(input('Digite o preço do produto: R$'))
total = preco
maisbarato = preco

if preco > 1000:
    maisdemil = 1

escolha = str(input('Você quer continuar? [Sim/Não] Digite: ')).strip().upper()[0]
while True:
    if escolha not in 'SN':
        escolha = str(input('Você quer continuar? [Sim/Não] Digite: ')).strip().upper()[0]
    else:
        break
if escolha == 'S':
    while True:
        prod = str(input('Digite o nome do produto: ')).strip()
        preco = float(input('Digite o preço do produto: R$'))

        if preco > 1000:
            maisdemil += 1

        if maisbarato > preco:
            maisbarato = preco
            prodmaisbarato = prod

        escolha = str(input('Você quer continuar? [Sim/Não] Digite: ')).strip().upper()[0]
        total += preco
        while True:
            if escolha not in 'SN':
                escolha = str(input('Você quer continuar? [Sim/Não] Digite: ')).strip().upper()[0]
            else:
                break
        if escolha == 'N':
            break
        print('----------//----------//----------')


print(f'{'  FIM DA COMPRA  ':-^40}')
print(f'O total da compra foi de R${total}')
print('{} produtos custaram mais de R$1000.00'.format(maisdemil))
print(f'O produto mais barato foi o(a) {prodmaisbarato} que custou R${maisbarato}')
