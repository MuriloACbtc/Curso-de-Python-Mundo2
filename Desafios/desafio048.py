
s = 0
for c in range(2, 501, 2):
    if c % 3 == 0:
        s = s + c
print("A soma é {}".format(s))
