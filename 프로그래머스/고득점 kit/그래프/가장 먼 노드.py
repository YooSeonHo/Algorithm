from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)

    
    for e in edge :
        a,b = e
        graph[b].append(a)
        graph[a].append(b)
        
    q = deque([])
    for g in graph[1] :
        q.append([g,0])
        
    visited[1] = 1
    while q:
        now,cnt = q.popleft()
        
        if not visited[now] :
            for g in graph[now] :
                q.append([g,cnt+1])
            visited[now] = cnt+1
            
    max_len = 0
    for v in visited :
        if max_len < v :
            max_len = v
    res = 0
    for v in visited :
        if v == max_len :
            res += 1
            
    return res
        

        
    