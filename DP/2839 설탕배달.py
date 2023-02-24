n = int(input())
dp = [-1] * 5001
dp[1] = 1
dp[3] = 1
dp[5] = 1

# def sugar(s):
#     if s<3 :
#         return 1000000
#     if s == 3 or s == 5:
#         return dp[s]
#     if dp[s] != 0 :
#         return dp[s]

    
#     dp[s] = min(sugar(s-3)+1,sugar(s-5)+1)
#     return dp[s]

# if n < 6 :
#     print(dp[n])
# else :
#     sugar(n)
#     print(dp[n])

for i in range(6,n+1):
    if dp[i-3] == -1 :
        if dp[i-5] != -1 :
            dp[i] = dp[i-5] + 1
    elif dp[i-5] == -1:
        if dp[i-3] != -1 :
            dp[i] = dp[i-3] + 1
    elif dp[i-3] != -1 and dp[i-5] != -1 :
        dp[i] = min(dp[i-3]+1,dp[i-5]+1)

print(dp[n])