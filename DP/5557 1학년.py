
n = int(input())
nums = list(map(int,input().split()))
res = nums[-1]
nums.pop()

dp = [[0] * 21 for _ in range(n)]
dp[1][nums[0]] = 1

for i in range(2,n) :
    for j in range(21) : 
        if 0<= j + nums[i-1] <= 20 :
            dp[i][j] += dp[i-1][j+nums[i-1]]
        
        if 0<= j - nums[i-1] <= 20 :
            dp[i][j] += dp[i-1][j-nums[i-1]]

        
print(dp[n-1][res])