from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    res = []
    
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    
    def bfs(y,x,num) :
        q = deque([])
        q.append([y,x,num])
        visited[y][x] = True
        cnt = 0
        cnt += int(num)
        while q :
            
            y,x,num = q.popleft()
            
            for i in range(4) :
                ny = y + dy[i]
                nx = x + dx[i]
                
                if 0<=ny<n and 0<=nx<m :
                    if not visited[ny][nx] and maps[ny][nx] != 'X' :
                        q.append([ny,nx,maps[ny][nx]])
                        visited[ny][nx] = True
                        cnt += int(maps[ny][nx])
                        
        return cnt
    
    for i in range(n) :
        for j in range(m) :
            if not visited[i][j] and maps[i][j] != 'X' :
                res.append(bfs(i,j,maps[i][j]))
                
    if len(res) == 0 :
        return [-1]
    else :
        res.sort()
        return res
            
            
        
            
    
    
    