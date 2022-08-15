from itertools import permutations

n = int(input())
arr = list(map(int,input().split()))

per = list(permutations(arr))

ans = 0

for p in per:
    tmp = 0
    for i in range(len(p)-1):
        tmp += abs(p[i]-p[i+1])
    
    if tmp > ans:
        ans = tmp

print(ans)
