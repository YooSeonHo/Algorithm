from collections import deque

n = int(input())
maze = [list(map(int,input().split())) for _ in range(n)]

# dy = [1,0]
# dx = [0,1]
# cnt = 0
# def bfs() :
#     global cnt
#     q = deque([])
#     q.append([0,0,maze[0][0]])

#     while q :
#         y,x,d = q.popleft()
        
#         for i in range(2):
#             ny = y + dy[i] * d
#             nx = x + dx[i] * d

#             if ny == n-1 and nx == n-1 :
#                 cnt += 1
#                 continue

#             if 0<=ny<n and 0<=nx<n :
#                 q.append([ny,nx,maze[ny][nx]])

# bfs()
# print(cnt)
# n <= 100 => 최대 2^10,000 메모리 ㅠㅠ
# 뭔가 "최단 경로"에 대한 문제가 아니고, 방문할 수 있는 모든 경우의 수를 구하는 문제니까
# visited 없이 풀어서 한 칸에 대해서도 방향에 따라 다 체크해줘야하는 문제가 발생
# visited 없이 bfs 돌리면 될 거 같은데? 라고 생각하는 순간 bfs 쓰면 안될듯
# idea https://breakcoding.tistory.com/361 참고

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):

        cur = maze[i][j]
        if cur == 0 :
            break

        if j + cur < n :
            dp[i][j+cur] += dp[i][j]
        if i + cur < n :
            dp[i+cur][j] += dp[i][j]

print(dp[n-1][n-1])


