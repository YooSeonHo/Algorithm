t = int(input())
k = int(input())
coins = []
for _ in range(k) : 
    coins.append(list(map(int,input().split())))
coins.sort()
# coin = 원 , 개수 순
dp = [[0] * (t+1) for _ in range(k)]

coin,num = coins[0]
dp[0][0] = 1
for j in range(1,num+1) :
    dp[0][coin * j] = 1

print(dp)

for i in range(1,k) :
    coin, num = coins[i]
    
    for c in range(t+1) :
        for j in range(1,num+1) :
            now = coin * j
            if 0 <= c+now <= t :
                dp[i][c+now] += dp[i-1][c]

print(dp)
