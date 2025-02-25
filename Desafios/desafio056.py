
somam20 = 0
somai = 0
hmaisvelho = 0
velho = ''
for c in range(1,5):
    print('===== {}ª Pessoa ====='.format(c))
    n = str(input('Digite seu nome: ')).strip()
    i = int(input('Digite sua idade em anos: '))
    s = str(input('Digite seu sexo, F para Feminino e M para Masculino: ')).lower().strip()
    somai = somai + i
    if s == "f" and i < 20:
        somam20 = somam20 + 1
    if s == 'm' and i > hmaisvelho:
        hmaisvelho = i
        velho = n

print('A \033[1;34mmédia de idade\033[m do grupo é de {} anos!'.format(somai/4))
print('O homem mais velho tem {} anos e se chama {}.'.format(hmaisvelho, velho))
print('{} mulher(es) tem \033[1;34mmenos de 20\033[m anos'.format(somam20))
