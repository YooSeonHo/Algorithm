from collections import deque


maps = ["SOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOLE"]

n = len(maps)
m = len(maps[0])
start = 0
leber = 0
end = 0
dy = [1,-1,0,0]
dx = [0,0,1,-1]

for i in range(n):
    for j in range(m) :
        if maps[i][j] == 'S' :
            start = [i,j,0]
        elif maps[i][j] == 'L' :
            leber = [i,j]
        elif maps[i][j] == 'E' :
            end = [i,j]

def bfs(start,search,maps) :
    global n,m
    visited = [[False] * m for _ in range(n)]
    q = deque([])
    q.append(start)
    y,x,cnt = start
    visited[y][x] = True
    flag = False
    while q :
        y,x,cnt = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0<= nx < m :
                print(ny,nx)
                if maps[ny][nx] != 'X' and not visited[ny][nx] :
                    if [ny,nx] == search :
                        flag = True
                        res = cnt + 1
                        return res
                    visited[ny][nx] = True
                    q.append([ny,nx,cnt+1])


    if not flag :
        return -1

tmp = bfs(start,leber,maps) 
if tmp == -1 :
    print(-1)
else :
    leber.append(tmp)
    print(bfs(leber,end,maps))