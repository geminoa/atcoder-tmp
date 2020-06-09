n = int(input().strip())
deck = list(reversed(sorted([int(i) for i in input().split()])))
a, b = 0, 0
flg = True
for c in deck:
    if flg: a += c
    else: b += c
    flg = not flg
print(a-b)
