from collections import deque

board = ["R...", "....", "....", "...G"]	
n = len(board)
m = len(board[0])
visited = [[False] * m for _ in range(n)]
me = 0
goal = 0
for i in range(n) :
    for j in range(m) :
        if board[i][j] == 'G' :
            goal = [i,j]
        if board[i][j] == 'R' :
            me = [i,j,0]

dy = [1,-1,0,0]
dx = [0,0,1,-1]
res = 0
flag = False
q = deque([])
q.append(me)
visited[me[0]][me[1]] = True
#벽 또는 장애물에 부딪히면, 부딪히기 전 위치가 내 위치
while q :
    y,x,cnt = q.popleft()
    for i in range(4):
        for j in range(1,max(n,m)+1) :
            ny = y + dy[i] * j
            nx = x + dx[i] * j
            if ny < 0 or ny >= n or nx < 0 or nx >= m or board[ny][nx] == 'D' :
                ny -= dy[i]
                nx -= dx[i]

                if board[ny][nx] == 'G' :
                    res = cnt + 1
                    flag = True
                    break

                if not visited[ny][nx] :
                    q.append([ny,nx,cnt+1])
                    visited[ny][nx] = True
                break


        if flag :
            break
    if flag :
        break

print(res if flag else -1)

    



