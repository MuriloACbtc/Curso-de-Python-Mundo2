
from random import randint
contador = 0
while True:
    computador = randint(1,10)
    jogador = int(input('Para jogar PAR ou ÍMPAR digite um número de 1 até 10: '))
    escolha = str(input('Escolha entre PAR ou ÍMPAR [P/I]: ')).upper().strip()[0]
    if escolha not in 'PI':
        while True:
            escolha = str(input('Escolha entre PAR ou ÍMPAR [P/I]: ')).upper().strip()[0]
            if escolha in 'IP':
                break
    soma = jogador + computador
    contador += 1
    if soma % 2 == 0 and escolha == 'P' or soma % 2 != 0 and escolha == 'I':
        print(f'computador: {computador} jogador: {jogador}, soma = {computador + jogador}')
        print('Parabéns você \033[1;32mGANHOU\033[m, jogue novamente')
    else:
        print(f'computador: {computador} jogador: {jogador}, soma = {computador + jogador}')
        print(f'Você \033[1;31mPERDEU\033[m, jogou {contador} jogos, e ganhou {contador-1} jogos.')
        break
