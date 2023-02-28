from collections import deque

arr = [[-1] * 102 for _ in range(102)]
visited = [[False] * 102 for _ in range(102)]
#1~100까지 ㅋ
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(characterX,characterY,itemX,itemY):
    q = deque([])
    q.append((characterX*2,characterY*2,0))
    visited[characterY*2][characterX*2]
    res = []
    while q:
        x,y,now = q.popleft()
        if x == itemX * 2 and y == itemY * 2 :
            res.append(now)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 1<= nx <= 100 and 1 <= ny <= 100 and not visited[ny][nx] and arr[ny][nx] == 1:
                q.append((nx,ny,now+1))
                visited[ny][nx] = True

    return (min(res)//2)




def solution(rectangle, characterX, characterY, itemX, itemY):
    #x좌표 -> col, y좌표 -> row
    
    for r in rectangle : 
        for i in range(r[1]*2, r[3]*2+1) :
            for j in range(r[0]*2,r[2]*2 + 1):
                if i == r[1]*2 or i == r[3] *2 or j == r[0]*2 or  j == r[2]*2 :
                    #테두리 처리
                    if arr[i][j] == 0 :
                        continue
                    elif arr[i][j] == -1 :
                        arr[i][j] = 1
                else :
                    arr[i][j] = 0

    return (bfs(characterX,characterY,itemX,itemY))
