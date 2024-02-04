import sys
input = sys.stdin.readline
n = int(input())
arr = [0] + list(map(int,input().split()))
q = int(input())

res = [0] * (n+1)
# 실수 = 1, 부를 수 있으면 0

part = [0] * (n+1)

for i in range(n) :
    if arr[i] > arr[i+1] :
        res[i] = 1

for i in range(1,n+1) :
    part[i] = part[i-1] + res[i]

for _ in range(q) :
    s,e = map(int,input().split())


    # 부분합 구하기
    ans = part[e] - part[s-1]
    if res[e] == 1:
        ans -= 1
    
    print(ans)