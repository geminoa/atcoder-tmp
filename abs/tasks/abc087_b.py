ary=[]
cnt=0
for i in range(0,4): ary.append(int(input()))
mvals = int(ary[3]/500), int(ary[3]/100), int(ary[3]/50)
for i in range(0,3): ary[i] = mvals[i] if ary[i] > mvals[i] else ary[i]

for i in range(ary[0], -1, -1):
    if 500*i >= ary[3]:
        if 500*i == ary[3]: cnt += 1
    else:
        rest = ary[3] - 500*i
        for j in range(ary[1], -1, -1):
            if 100*j >= rest:
                if 100*j == rest: cnt += 1
            else:
                rest2 = rest - 100*j
                for k in range(ary[2], 0, -1):
                    if 50*k >= rest2:
                        if 50*k == rest2: cnt += 1
print(cnt)
