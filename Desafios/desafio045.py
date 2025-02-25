import random
print('Jokenpô')
a = str(input('Digite pedra, papel, ou tesoura: ')).lower().strip()
lista = ['papel', 'tesoura', 'pedra']
comp = random.choice(lista)
if a == comp:
    print('\033[1;33mEMPATOU!\033[m\nVocê e o computador escolheram \033[1m{}\033[m'.format(a))

elif a == 'pedra' and comp == 'tesoura' or a == 'papel' and comp == 'pedra' or a == 'tesoura' and comp == 'papel':
    print('\033[1;34mPARABÉNS!\033[m\nVocê ganhou! \033[34m{}\033[m ganha do(a) \033[31m{}\033[m'.format(a, comp))

else:
    print('\033[1;31mVocê PERDEU!\033[m\n\033[34m{}\033[m ganha do(a) \033[31m{}\033[m'.format(comp, a))
