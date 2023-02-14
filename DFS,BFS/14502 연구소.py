from collections import deque
import copy

dx = [1,0,-1,0]
dy = [0,1,0,-1]

n,m = map(int,input().split())
yeon = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
virus = []
res = []

for x in range(n):
    for y in range(m):
        if yeon[x][y] == 2 :
            virus.append((x,y))

def bfs():

    arr = copy.deepcopy(yeon)
    vis = copy.deepcopy(visited)
    q = deque([])
    for v in virus :
        virusx = v[0]
        virusy = v[1]
        q.append((virusx,virusy))
        vis[virusx][virusy] = True

    while q:
        r,c = q.popleft()

        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]

            if 0<=nx<n and 0<=ny<m :
                if not vis[nx][ny] and arr[nx][ny] != 1 :
                    q.append((nx,ny))
                    vis[nx][ny] = True
                    arr[nx][ny] = 2

    cnt = 0
    for a in range(n):
        for b in range(m):
            if arr[a][b] == 0 :
                cnt += 1
    res.append(cnt)

for q in range(n):
    for w in range(m):
        if yeon[q][w] == 0 :
            yeon[q][w] = 1

            for e in range(n):
                for r in range(m):
                    if yeon[e][r] == 0 :
                        yeon[e][r] = 1

                        for t in range(n):
                            for y in range(m):
                                if yeon[t][y] == 0:
                                    yeon[t][y] = 1
                                    bfs()

                                    yeon[t][y] = 0

                        yeon[e][r] = 0

            yeon[q][w] = 0
print(max(res))



