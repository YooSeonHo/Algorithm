import sys
input = sys.stdin.readline

n,m = map(int,input().split())

arr = list(map(int,input().split()))
dp = [0] * (n+1)
dp[1] = arr[0]
for i in range(1,n+1) :
    dp[i] = dp[i-1] + arr[i-1]

for _ in range(m) : 
    a,b = map(int,input().split())
    if a == b :
        print(arr[b-1])
    else : 
        print(dp[b] - dp[a-1])