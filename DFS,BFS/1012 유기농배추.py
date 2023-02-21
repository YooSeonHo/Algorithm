from collections import deque

t = int(input())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y,visited):
    q = deque([])
    q.append((x,y))
    visited[x][y] = True
    while q:
        a,b = q.popleft()

        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]

            if 0<=nx<row and 0<=ny<col and not visited[nx][ny] and arr[nx][ny] == 1 :
                q.append((nx,ny))
                visited[nx][ny] = True



for _ in range(t):
    col,row,bae = map(int,input().split())
    arr = [[0] * col for _ in range(row)]
    visited = [[False] * col for _ in range(row)]
    res = 0

    for _ in range(bae):
        a,b = map(int,input().split())
        arr[b][a] = 1

    for a in range(row):
        for b in range(col):
            if not visited[a][b] and arr[a][b] == 1 :
                bfs(a,b,visited)
                res +=1
    print(res)
