import sys
input = sys.stdin.readline
# 시간 제한 0.1초;;

n,k,q,m = map(int,input().split())
sleep = set(map(int,input().split()))
check = set(map(int,input().split()))
loc = []

for _ in range(m) :
    s,e = map(int,input().split())
    loc.append([s,e])

check_list = [0] * (n+3)

for c in (check-sleep) :
    for i in range(c,n+3,c) :
        if i not in sleep :
            check_list[i] = 1

ans = [0] * (n+3)
for i in range(3,n+3) :
    ans[i] = ans[i-1] + check_list[i]

for l in loc :
    res = (l[1]-l[0]+1) - (ans[l[1]] - ans[l[0]-1])
    print(res)



