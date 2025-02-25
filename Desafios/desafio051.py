
p = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
for c in range(p, p+(r*10)+1, r):
    print(c, end=" -> ")
