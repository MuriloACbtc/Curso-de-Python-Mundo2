
frase = str(input('Digite uma frase: ')).upper().strip()
dividido = frase.split()
j = ''.join(dividido)
nelementos = len(j)

'''inverso = ''
                        # V  o primeiro elemento é 0, então se subtrai 1
for c in range(nelementos - 1, -1, -1):
    inverso = inverso + j[c]
    ou'''
inverso = j[::-1]#[::-1] representa o inverso de uma frase/algo


if inverso == j:
    print('Temos um palíndromo\n{} e {}'.format(j, inverso))
else:
    print('Não temos um palindromo\n{} e {}'.format(j, inverso))