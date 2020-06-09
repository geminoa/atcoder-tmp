total = 0
ary = [int(i) for i in input().split()]
for i in range(ary[1], ary[0]+1):
    digits = int(i/10000)%10, int(i/1000)%10, int(i/100)%10, int(i/10)%10, i%10
    sum_d = sum(digits)
    if sum_d >= ary[1] and sum_d <= ary[2]:
        total += i
print(total)
