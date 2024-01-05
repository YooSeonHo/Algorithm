import sys
input = sys.stdin.readline

n = int(input())

meeting = [list(map(int,input().split())) for _ in range(n)]
dp = [0] * n
dp[0] = meeting[0][2]
if n >= 2 :
    dp[1] = meeting[1][2]
    if n >= 3 :
        dp[2] = dp[0] + meeting[2][2]

for i in range(3,n) :
    dp[i] = max(dp[i-2],dp[i-3]) + meeting[i][2]

print(max(dp))
