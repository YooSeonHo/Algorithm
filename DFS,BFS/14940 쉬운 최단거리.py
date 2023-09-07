from collections import deque
n,m = list(map(int,input().split()))

graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dy = [1,-1,0,0]
dx = [0,0,1,-1]

q = deque([])

flag = False
for i in range(n):
    for j in range(m) :
        if graph[i][j] == 2 :
            q.append([i,j,0])
            graph[i][j] = 0
            visited[i][j] = True
            flag = True
            break
    if flag :
        break

while q :
    y,x,cnt = q.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= n or nx < 0 or nx >= m :
            continue
        else :
            if not visited[ny][nx] :
                if graph[ny][nx] != 0 :
                    q.append([ny,nx,cnt+1])
                    visited[ny][nx] = True
                    graph[ny][nx] = cnt +1
                else :
                    visited[ny][nx] = True

for i in range(n):
    for j in range(m):
        if visited[i][j] :
            continue
        else :
            if graph[i][j] == 0 :
                continue
            else :
                graph[i][j] = -1


for g in graph :
    print(*g)