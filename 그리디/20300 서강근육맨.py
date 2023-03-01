import sys
input = sys.stdin.readline

n = int(input())
t = list(map(int,input().split()))
t.sort()
res = []
if n % 2 == 0 :
    for i in range(n//2):
        tmp = t[i] + t[n-1-i]
        res.append(tmp)
else :
    for i in range((n-1)//2):
        tmp = t[i] + t[n-2-i]
        res.append(tmp)

    res.append(t[n-1])

print(max(res))