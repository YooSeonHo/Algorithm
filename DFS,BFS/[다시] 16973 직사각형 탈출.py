import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
maze = [list(map(int,input().split())) for _ in range(n)]
h,w,sr,sc,fr,fc = map(int,input().split())
# 직사각형의 크기 H, W, 시작 좌표 Sr, Sc, 도착 좌표 Fr, Fc
    
dy = [1,-1,0,0]
dx = [0,0,1,-1]

sr -= 1
sc -= 1
fr -= 1
fc -= 1

walls = []
for i in range(n) :
    for j in range(m) :
        if maze[i][j] == 1 :
            walls.append([i,j])

# partial_maze = [[0] * (m+1) for _ in range(n+1)]
# for i in range(1,n+1) :
#     for j in range(1,m+1) :
#         partial_maze[i][j] = partial_maze[i-1][j] + partial_maze[i][j-1] - partial_maze[i-1][j-1] + maze[i-1][j-1]

# maze = (0,0) ~ (n-1,m-1)
# partial = (1,1) ~ (n,m)

# def partial(y,x,h,w) :
# #    (y,x) ~ (y+h,x+w) 까지의 부분합 구하기
#     partial_y = y+h-1
#     partial_x = x+w-1

#     if not 1 <= partial_y <= n or not 1 <= partial_x <= m :
#         return True 
#     res = partial_maze[partial_y][partial_x] - partial_maze[y-1][partial_x] - partial_maze[partial_y][x-1] + partial_maze[y-1][x-1]
#     return res

def check(y,x) :
    for wall in walls :
        cy,cx = wall
        if y <= cy < y+h and x <= cx < x + w :
            return False
    return True

q = deque([])
visited = [[0] * (m) for _ in range(n)]
q.append([sr,sc,0])
visited[sr][sc] = 1

while q:
    y,x,cnt = q.popleft()

    if y == fr and x ==fc :
        break
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<= ny and ny+h-1 < n and 0 <= nx and nx+w-1 < m :
            if not visited[ny][nx] :
                if check(ny,nx) :
                    q.append([ny,nx,cnt+1])
                    visited[ny][nx] = cnt+1

print(visited[fr][fc] if visited[fr][fc] else -1)