print('\033[1;36m/\033[35m--\033[m'*10)
print('\033[1;37mÍndice de Massa Corporal')
print('\033[1;35m/\033[36m--\033[m'*10)
peso = float(input('Digite apenas o número do seu peso em kg: '))
altura = float(input('Digite apenas o número de sua altura em metros: '))
imc = peso/(altura**2)
print('Seu IMC é {}'.format(imc))
if imc < 18.5:
    print('Você está \033[1;33mABAIXO DO PESO!\033[m')
elif imc <= 25:
    print('Você está no \033[1;32mPESO IDEAL!\033[m')
elif imc <= 30:
    print('Você está com \033[1;33mSOBREPESO!\033[m')
elif imc <= 40:
    print('Você está com \033[1;31mOBESIDADE!\033[m')
else:
    print('Você está com \033[1;4;30;41mOBESIDADE MÓRBIDA!\033[m')
