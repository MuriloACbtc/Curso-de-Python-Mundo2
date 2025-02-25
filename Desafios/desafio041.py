

from datetime import date
anoatual = date.today().year
nascimento = int(input('Digite o ano em que você nasceu: '))
idade = anoatual - nascimento
print(idade)

'''print('\033[1;34mCONFEDERAÇÃO NACIONAL DE \033[36mNATAÇÃO\033[m')
i = int(input('Digite sua idade em anos: '))
if i <= 9:
    print('Sua categoria é \033[1;33mMIRIM\033[m!')
elif i <= 14:
    print('Sua categoria é \033[1;32mINFANTIL\033[m')
elif i <= 19:
    print('Sua categoria é \033[1;36mJUNIOR\033[m')
elif i <= 20:
    print('Sua categoria é \033[1;34mSÊNIOR\033[m')
else:
    print('Sua categoria é \033[1;35mMASTER\033[m')'''
