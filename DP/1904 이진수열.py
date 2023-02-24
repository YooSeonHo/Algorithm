import sys
sys.setrecursionlimit(10 ** 6)
n = int(input())
dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1


# def fibo(n):
#     if n == 1 or n == 0 :
#         return dp[n]
#     if dp[n] != 0 :
#         return dp[n]

#     dp[n] = (fibo(n-1) + fibo(n-2) % 15746)
#     return dp[n] 

# fibo(n)
for i in range(2,n+1):
    dp[i] = ((dp[i-1] + dp[i-2]) % 15746)

print(dp[n])