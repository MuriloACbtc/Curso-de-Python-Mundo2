
while True:
    n = int(input('Quer ver a tabuada de qual valor? Digite aqui: '))
    print('-------------------------------------------------------')
    c = 0
    if n < 0:
        print('Você parou!')
        break
    while True:
        print(f'{n} x {c} = {n*c}')
        c += 1
        if c == 11:
            break
    print('-------------------------------------------------------')