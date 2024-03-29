import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

n,m = len(a), len(b)

dp = [[0] * (m+1) for _ in range(n+1)]

res = 0
for i in range(1,n+1) :
    for j in range(1,m+1) :
        if a[i-1] == b[j-1] :
            dp[i][j] = dp[i-1][j-1] + 1
            res = max(res,dp[i][j])


print(res)      