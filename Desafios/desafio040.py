print('\033[37;40mSISTEMA DE NOTAS\033[m')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1+n2)/2
if m < 5:
    print('Sua nota média foi abaixo de 5\nVocê foi \33[1;31mREPROVADO!\033[m')
elif m >= 7:
    print('Sua nota média foi superior a 7\nVocê foi \033[1;32mAPROVADO!\033[m')
else:
    print('Sua nota média ficou entre 5.0 e 6.9\nVocê ficou de \033[1;33mRECUPERAÇÃO!\033[m')
