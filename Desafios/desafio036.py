

print('\033[1;7;33mSistema de Empréstimo para a Compra de Casas\033[m')
v = float(input('Digite o valor da casa em:\033[32m R$\033[m'))
s = float(input('Digite o seu salário mensal:\033[32m R$\033[m'))
a = float(input('Digite em \033[1mquantos anos você pretende pagar\033[m: '))
prestacao = v/(a * 12)
print('O valor da prestação é de \033[1;32mR${:.2f}\033[m'.format(prestacao))
if prestacao/s <= 0.3:
    print('O \033[35memprestimo\033[m foi \033[1;32maprovado com sucesso\033[m!')
else:
    print('Como sua prestação mensal é maior que 30% do seu salário, \nSeu \033[35mempréstimo\033[m foi \033[1;31mnegado\033[m!')
