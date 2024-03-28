import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
ans = arr[-1]
arr.pop()

dp = [[0] * 21 for _ in range(n)]
dp[1][arr[0]] = 1

for i in range(2,n):
    for j in range(21) :
        if 0 <= j + arr[i] <= 20 :
            dp[i][j] += dp[i-1][j+arr[i]]
