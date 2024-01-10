from collections import deque

def solution(maps):
    n,m = len(maps), len(maps[0])
    
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    q = deque([])
    
    visited = [[False] * m for _ in range(n)]
    ans = 0
    
    q.append([0,0,1])
    visited[0][0] = True
    
    while q:
        y,x,cnt = q.popleft()
        print(y,x,cnt)
        
        if y == n-1 and x == m-1 :
            ans = cnt
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0<= ny <n and 0 <= nx < m :
                if not visited[ny][nx] and maps[ny][nx] :
                    q.append([ny,nx,cnt+1])
                    visited[ny][nx] = True
                
    if ans == 0 :
        return -1
    else :
        return ans