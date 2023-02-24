n = int(input())
arr = []
dp = [0] * (n+1)
for _ in range(n):
    a,b = list(map(int,input().split()))
    arr.append((a,b))

for i in range(n-1,-1,-1):
    if arr[i][0] + i > n :
        dp[i] = dp[i+1]
    else :
        dp[i] = max(dp[i+1],dp[i+arr[i][0]] + arr[i][1])

print(dp[0])