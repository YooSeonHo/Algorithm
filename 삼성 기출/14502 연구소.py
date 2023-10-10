from collections import deque
import copy

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
virus = []
dy = [1,-1,0,0]
dx = [0,0,1,-1]
res = 0


def virus_check(arr,virus) :
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2 :
                virus.append([i,j])

def safe_check(arr) : 
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0 :
                cnt += 1

    return cnt

def safe_zone(arr) :
    safe = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0 :
                safe.append([i,j])

    return safe


def bfs(arr_original) : 
    global res, virus
    arr = copy.deepcopy(arr_original)
    visited = [[False] * m for _ in range(n)]
    q = deque(virus)
    
    while q :
        y,x = q.popleft()
        visited[y][x] = True
        
        for i in range(4) :
            ny =  y + dy[i]
            nx =  x + dx[i]

            if 0<=ny<n and 0<=nx<m :
                if not visited[ny][nx] and arr[ny][nx] == 0 : 
                    q.append([ny,nx])
                    visited[ny][nx] = True
                    arr[ny][nx] = 2

    res = max(res,safe_check(arr))  

virus_check(arr,virus)

# 벽 세울 위치 3개 찾는거 어케하지? 조합 라이브러리 안쓰고........ => 미친 6중 포문 썼네 옛날에
# for a in range(n) :
#     for b in range(m) :
#         if arr[a][b] == 0 :
#             arr[a][b] = 1

#             for c in range(n) :
#                 for d in range(m) :
#                     if arr[c][d] == 0 :
#                         arr[c][d] = 1

#                         for e in range(n) :
#                             for f in range(m) :

#                                 if arr[e][f] == 0 :
#                                     arr[e][f] = 1
#                                     bfs(arr)
#                                     arr[e][f] = 0
#                         arr[c][d] = 0
#             arr[a][b] = 0
            

def make_wall(cnt) : 
    if cnt == 3 :
        bfs(arr)
        return
    else :
        for i in range(n):
            for j in range(m) :
                if arr[i][j] == 0 :
                    arr[i][j] = 1
                    make_wall(cnt+1)
                    arr[i][j] = 0



make_wall(0)
print(res)