
s = str(input('Digite seu sexo, M ou F: ')).strip().upper()[0]
while s not in 'MmFf':
    print('Você digitou \033[1;31merrado\033[m')
    s = str(input('Digite novamente \033[1mM ou F\033[m: ')).upper().strip()[0]
print('\033[1;33mParabéns\033[m, você digitou corretamente!')
