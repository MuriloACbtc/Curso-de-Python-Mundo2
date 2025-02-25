
c = h = ms = 0
while True:
    print('------- Cadastrar UMA pessoa -------')
    idade = int(input('Digite a idade da pessoa: '))
    if idade >= 18:
        c += 1
    sexo = str(input('Digite o sexo da pessoa [F/M]: ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa [F/M]: ')).upper().strip()[0]

    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        ms += 1
    print('==--==--==--==--==--==--==--==--==--==--==--==--==--==--==--==')
    escolha = str(input('Quer continuar? [Sim/Não] Digite: ')).upper().strip()[0]
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [Sim/Não] Digite: ')).upper().strip()[0]

    if escolha == 'N':
        break
print('======== FIM DO PROGRAMA ========')
print(f'''{c} pessoas tem mais de \033[1;34m18 anos\033[m.
{h} \033[1;33mhomens\033[m foram cadastrados.
{ms} \033[1;33mmulheres\033[m tem menos de \033[1;34m20 anos\033[m.
''')