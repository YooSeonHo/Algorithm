from collections import deque
n,m = map(int,input().split())
maze = [list(map(int,input())) for _ in range(n)]

dx = [-1,0,0,1]
dy = [0,1,-1,0]

def bfs():
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    q = deque([(0,0,1)])

    while q:
        x, y, cnt = q.popleft()
        
        if x == n-1 and y == m-1 :
            print(cnt)
            break
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                    continue
                elif maze[nx][ny] == 0 :
                    continue
                elif visited[nx][ny] == True:
                    continue
                else :
                    q.append((nx,ny, cnt+1))
                    visited[nx][ny] = True

bfs()

