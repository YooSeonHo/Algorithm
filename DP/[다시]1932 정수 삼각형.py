


n = int(input())
triangle = [ list(map(int,input().split())) for _ in range(n)]
dp = [[0] * (n) for _ in range(n)]
dp[0][0] = triangle[0][0]

for i in range(1,n) :
    for j in range(i+1) :
        if j == 0 :
            dp[i][j] = dp[i-1][j] + triangle[i][j]
            continue
        
        if j == i+1 :
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            continue

        dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]) + triangle[i][j]

print(max(dp[-1]))
        


















# import sys
# input = sys.stdin.readline

# n = int(input())
# t = []
# res = []
# for _ in range(n):
#     li = list(map(int,input().split()))
#     t.append(li)

# res.append(t[0])

# for i in range(1,n):
#     tmp = []
#     for j in range(len(t[i-1])):
#         left = res[i-1][j] + t[i][j]
#         right = res[i-1][j] + t[i][j+1]
#         tmp.append(left)
#         tmp.append(right)

#     res.append(tmp)
# print(res)
# # print(max(res[n-1]))