cnt = 0
n = int(input())
ary = [int(i) for i in input().split() if int(i) % 2 == 0]
while len(ary) == n:
    ary = [i/2 for i in ary if i % 2 == 0]
    if len(ary) != n: break
    cnt += 1
print(cnt)
