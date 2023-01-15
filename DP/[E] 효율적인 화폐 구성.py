n,m = map(int,input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [0] * 100001

for i in range(len(coins)):
    dp[coins[i]] = 1

#dp[1] dp[5] dp[12] = 1

for i in range(1,m+1):
    if dp[i] == 1:
        continue
    minNum = 100001
    for coin in coins :
        if i > coin and dp[i-coin] != 0 and minNum > dp[i-coin]+1 :
            minNum = dp[i-coin]+1

    if minNum == 100001:
        dp[i] = 0
    else :
        dp[i] = minNum

if dp[m] == 0 :
    print(-1)
else :
    print(dp[m])
            

# 1인 애들을 0으로 만들어 버리는거, 