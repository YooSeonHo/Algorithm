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