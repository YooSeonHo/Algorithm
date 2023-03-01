import sys
input = sys.stdin.readline

n = int(input())
d = list(map(int,input().split()))
p = list(map(int,input().split()))

# d[0] => p[0]~p[1] 사이 거리
# d[1] => p[1]~p[2] 사이 거리

res = 0
tmp = 0

min = 0
for i in range(1,n-1) :
    if p[min] >= p[i] :
        res += sum(d[min:i]) * p[min] 
        min = i
    else :
        continue

if min != n-1 :
    res += sum(d[min:n]) * p[min] 

print(res)