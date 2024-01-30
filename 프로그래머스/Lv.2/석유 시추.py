from collections import deque

def bfs(land,visited,y,x,num) :
    n = len(land)
    m = len(land[0])
    
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    q = deque([])
    
    q.append([y,x])
    visited[y][x] = num
    cnt  = 1
    
    while q:
        ty,tx = q.popleft()
        for i in range(4):
            ny = ty + dy[i]
            nx = tx + dx[i]
            if 0 <= ny < n and 0 <= nx < m :
                if not visited[ny][nx] and land[ny][nx] :
                    q.append([ny,nx])
                    cnt += 1
                    visited[ny][nx] = num
    return cnt               
    
                    

def solution(land):
    num = 1
    n = len(land)
    m = len(land[0])
    visited = [[0] * m for _ in range(n)]
    res = []
    ans = 0
    
    for i in range(n) :
        for j in range(m) :
            if land[i][j] and not visited[i][j] :
                res.append(bfs(land,visited,i,j,num))
                num += 1
    
    for i in range(m) :
        tmp = []
        tmpAns = 0
        for j in range(n) :
            if visited[j][i] and visited[j][i] not in tmp :
                tmp.append(visited[j][i])
        
        for t in tmp :
            tmpAns += res[t-1]
        ans = max(ans,tmpAns)
        
    return (ans)