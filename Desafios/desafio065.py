

resposta = 'sim'
s = 0
maior = 0
menor = 0
nn = 0

while resposta == 'sim':
    n = float(input('Digite um número: '))
    s += n
    nn = nn + 1
    if nn == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resposta = str(input('Quer continuar? Escreva sim ou não: ')).lower()

media = s/nn
print('Você parou.\nA \033[1;33mmédia entre todos\033[m os valores foi de {}.'.format(media))
print('O maior valor foi o {}, e o menor foi o {}.'.format(maior, menor))
