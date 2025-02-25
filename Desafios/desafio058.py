
from random import randint
print('\033[1;34m+=+{}[]+=+\033[31m+=+{}[]+=+\033[m'*4)
print('\033[1;7;34mTente acertar o número inteiro que o \033[31mcomputador pensou de 1 até 10\033[m')
print('\033[1;34m-=-=\033[31m-=-=\033[m'*10)


n = randint(1, 10)
palpite = int(input('Digite seu palpite: '))
tentativas = 1
while palpite != n:
    print('Você \033[1;31merrou\033[m, colocou {}.'.format(palpite))
    palpite = int(input('Tente novamente, de 1 até 10: '))
    tentativas += 1

print('\033[1;32mParabéns!\033[m Você acertou com \033[1;33m{}\033[m tentativas'.format(tentativas))
