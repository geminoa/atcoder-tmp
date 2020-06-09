ps = [[0,0,0]]
n = int(input())
for i in range(0, n):
    ps.append([int(i) for i in input().split()])

def dst(p1x,p1y,p2x,p2y):return abs(p2x-p1x)+abs(p2y-p1y)

for i in range(0, len(ps)-1):
    d = dst(ps[i][1], ps[i][2], ps[i+1][1], ps[i+1][2])
    if (ps[i+1][0]-ps[i][0] < d) or ((ps[i+1][0]-ps[i][0] - d)%2 != 0):
        print('No')
        exit()
print('Yes')
