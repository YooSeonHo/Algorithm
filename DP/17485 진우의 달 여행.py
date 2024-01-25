import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
INF = 1234567890
dp = [[[INF] * 3 for _ in range(m)]  for _ in range(n)]

for i in range(m) :
    for j in range(3) :
        dp[0][i][j] = arr[0][i]

for i in range(1,n) :
    for j in range(m) :
        for k in range(3) :
            dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + arr[i][j]
            if j == 0 :
                dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2]) + arr[i][j]
            elif j == m-1 :
                dp[i][j][2] = min(dp[i-1][j-1][0], dp[i-1][j-1][1]) + arr[i][j]
            else :
                dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2]) + arr[i][j]
                dp[i][j][2] = min(dp[i-1][j-1][0], dp[i-1][j-1][1]) + arr[i][j]
ans = INF
for d in dp[-1] : 
    ans = min(min(d),ans)
print(ans)
# for i in range(1,n) :
#     for j in range(m) :
#         tmp = []
#         a = dp[i-1][j]
#         if a[1] != 2 :
#             tmp.append([a[0] + arr[i][j],2])
    
#         if j == 0 :
#             b = dp[i-1][j+1]
#             if b[1] != 3 :
#                 tmp.append([b[0] + arr[i][j],3])
#         elif j == m-1 :
#             c = dp[i-1][j-1]
#             if c[1] != 1 :
#                 tmp.append([c[0] + arr[i][j],1])
#         else :
#             b = dp[i-1][j+1]
#             c = dp[i-1][j-1]
#             if b[1] != 3 :
#                 tmp.append([b[0] + arr[i][j],3])
#             if c[1] != 1 :
#                 tmp.append([c[0] + arr[i][j],1])

#         dp[i][j] = min(tmp)

# print(min(dp[n-1])[0])