
s = 0
for c in range(0, 6):
    n = int(input())
    if n % 2 != 0:
        n = 0
    else:
        n = n
    s = s + n
print(s)
