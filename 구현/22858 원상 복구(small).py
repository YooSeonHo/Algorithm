import sys
input = sys.stdin.readline

n,k = map(int,input().split())
s = list(map(int,input().split()))
d = list(map(int,input().split()))
res = [0] * (n )
#d에 index와 value가 있다고 할때 우린 value를 보고 value번째 카드를 index번째 카드로 보냄
# 우린 역순으로 d의 index를 보고 s의 index번째 카드를 value로


for _ in range(k):
    for i in range(n):
        res[d[i]-1] = s[i]
    
    s = res.copy()

print(*res)

