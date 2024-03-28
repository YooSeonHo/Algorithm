from collections import deque

def solution(n, computers):
    
    coms = [[] for _ in range(n)]
    visited = [False] * n
    res = 0
    
    for i,com in enumerate(computers) :
        for j,c in enumerate(com) :
            if i == j :
                continue
            if c == 1 :
                coms[i].append(j)
                
    for i in range(n) :
        if not visited[i] :
            res += 1
            q = deque([])
            q.append(i)
            visited[i] = True
            
            while q:
                now = q.popleft()
                
                for c in coms[now] :
                    if not visited[c] :
                        q.append(c)
                        visited[c] = True
                        
    return (res)