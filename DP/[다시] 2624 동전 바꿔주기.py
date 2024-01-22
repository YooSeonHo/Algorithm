import sys
input = sys.stdin.readline

t = int(input())
k = int(input())
coins = [list(map(int,input().split())) for _ in range(k)]
# [0] = 금액, [1] = 코인 개수
dp = [0] * (t+1)
dp[0] = 1

for coin,num in coins :
    for money in range(t,0,-1) :
        for i in range(1,num+1) :
            if money - coin * i >= 0:
                dp[money] += dp[money - coin * i]

print(dp[t])

# 혼자 풀이법 생각하기 힘들 거 같은데.... 