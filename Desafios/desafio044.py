print('\033[31m*-*-\033[m'*8)
print('\033[1mValor a ser pago pelo produto\033[m')
print('\033[34m-*-*\033[m'*8)
p = float(input('Digite o valor do produto: R$'))
f = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque (10% de desconto)
[ 2 ] à vista cartão (5% de desconto)
[ 3 ] 2x no cartão (preço normal)
[ 4 ] 3x ou mais no cartão (20% de juros)
Digite o número da opção escolhida: '''))
if f == 1:
    print('O preço a se pagar vai de R${} para R${}.'.format(p, p*0.9))
elif f == 2:
    print('O preço a se pagar vai de R${} para R${}.'.format(p, p*0.95))
elif f == 3:
    print('O preço a se pagar é R${}, em 2 parcelas de R${}.'.format(p, p/2))
elif f == 4:
    parcelas = int(input('Digite a quantidade de parcelas: '))
    print('O preço a se pagar vai de R${} para R${}, com {} parcelas de R${}'.format(p, p*1.2, parcelas, p*1.2/parcelas))

else:
    print('Escolha uma opção correta')
