
print('='*40)
print(f'{' BANDO DO MURILO ':^40}')
print('='*40)

v = int(input('Digite qual valor você quer sacar: R$'))
print('$$'*20)
c50 = v//50
print(c50, 'cédula(s) de R$50')
v = v - c50*50
c20 = v//20
print(c20, 'cédula(s) de R$20')
v = v - c20*20
c10 = v//10
print(c10, 'cédula(s) de R$10')
v = v - c10*10
print(v, 'cédula(s) de R$1')