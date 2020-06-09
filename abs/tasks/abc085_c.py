res = ['-1', '-1', '-1']
units = [10000, 5000, 1000]
n, y = [int(i) for i in input().split()]
for i in range(0, n+1):
    for j in range(0, n+1-i):
        k = n - i - j
        if y == i*10000 + j*5000 + k*1000:
            res = [str(i), str(j), str(k)]
            break
print(' '.join(res))
