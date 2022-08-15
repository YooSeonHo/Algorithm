import sys
imput = sys.stdin.readline
from itertools import permutations

n = int(imput())
W = [list(map(int,imput().split())) for _ in range(n)]

per = list(permutations(range(1,n)))

ans = 1e9

for p in per:
    flag = True
    tmp = 0
    p = list(p)
    p.append(0)
    p.insert(0,0)

    for i in range(len(p)-1):
        if W[p[i]][p[i+1]] :
            tmp += W[p[i]][p[i+1]]
        else:
            flag = False
            break
    if not flag :
        continue
    else:
        if ans > tmp:
            ans = tmp

print(ans)

