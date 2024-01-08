n = int(input())

dp = [0] * 100001
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
dp[5] = 1
dp[6] = 2
dp[7] = 1

for i in range(8,100001) :
    dp[i] = min(dp[i-1],dp[i-2],dp[i-5],dp[i-7]) + 1

print(dp[n])


################## 정석 풀이 ###################################

n = int(input())
dp = [i for i in range(n+1)]

for i in range(2,n+1):
    dp[i] = dp[i-1] + 1
    if i >= 2 :
        dp[i] = min(dp[i],dp[i-2]+1)
    if i >= 5:
        dp[i] = min(dp[i],dp[i-5]+1)
    if i >= 7 :
        dp[i] = min(dp[i],dp[i-7]+1)

print(dp[n])