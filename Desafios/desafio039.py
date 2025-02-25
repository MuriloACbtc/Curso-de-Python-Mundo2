print('\033[1;32mALISTAMENTO MILITAR\033[m')
s = str(input('Digite o seu sexo, M para masculino e F para feminino: ')).lower()
i = int(input('Digite sua idade em anos: '))
if s == 'm':
    if i < 18:
        print('\033[33mVocê ainda vai se alistar!\033[m')
        if i == 17:
            print('\033[32mFalta 1 ano para o seu alistamento\033[m')
        else:
            print('\033[32mFaltam {} anos para o seu alistamento\033[m'.format(18-i))
    elif i == 18:
        print('\033[1;32mEsse é o ano para você se alistar!\033[m')
    else:
        print('\033[7;40mJá passou do tempo do seu alistamento!\033[m')
        if i == 19:
            print('\033[32mSe passou 1 ano do seu alistamento')
        else:
            print('\033[32mSe passaram {} anos do seu alistamento\033[m'.format(i-18))
elif s == 'f':
    print('\033[32mVocê \033[1mnão precisa\033[0;32m se alistar\033[m, fique tranquila, se quiser se alistar, entre em contato no site')
else:
    print('Digite corretamente')
