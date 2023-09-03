# import sys
# from collections import deque
# input = sys.stdin.readline

# n,m,r = map(int,input().split())

# arr = [list(map(int,input().split())) for _ in range(n)]
# q = deque([])
# for i in range(min(n,m)//2) :
#     q.clear()
#     q.extend(arr[i][i:m-i])
#     q.extend(arr[i+1:n-1-i][m-i-1])
#     q.extend(arr[n-i-1][i:m-i][::-1])
#     q.extend(arr[n-i-1][n-i-2:i+1:-1])

#     q.rotate(-r)
#     print(q)