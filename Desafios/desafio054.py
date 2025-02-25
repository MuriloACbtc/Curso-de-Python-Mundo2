
import datetime
smaior = 0
smenor = 0
for c in range(0, 7):
    n = int(input('Digite seu ano de nascimento: '))
    i = datetime.date.today().year - n
    if i >= 21:
        print('Você com {} anos é maior de idade, tem mais de 21 anos!'.format(i))
        smaior += 1
    else:
        print('Você com {} anos é menor de idade, tem menos de 21 anos!'.format(i))
        smenor += 1
print('{} pessoas tem menos de 21 anos, e {} pessoas tem mais de 21 anos.'.format(smenor, smaior))
