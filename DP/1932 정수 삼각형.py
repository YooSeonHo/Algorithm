import sys
input = sys.stdin.readline

n = int(input())
triangle = [list(map(int,input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = triangle[0][0]

for i in range(1,n) :
    for j in range(n) :
        if j == 0 :
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        elif j == len(triangle[i]) -1 :
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            break
        else :
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]

print(max(dp[-1]))

