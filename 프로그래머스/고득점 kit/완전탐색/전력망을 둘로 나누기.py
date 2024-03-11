from collections import deque

def solution(n, wires):
    
    def bfs(start,cnt) :
        q = deque([])
        q.append((start,cnt))
        visited[start] = 1
        counting = []
        while q:
            now,now_cnt = q.popleft()
            counting.append(now_cnt)
            
            for t in tree[now] :
                if not visited[t] :
                    q.append((t,now_cnt+1))
                    visited[t] = 1
        return len(counting)
    
    res = []
    
    for i in range(n-1) :
        tree = [[] for _ in range(n+1)]
        visited = [0] * (n+1)

        for j in range(n-1) :
            if i == j : 
                continue
            a = wires[j][0]
            b = wires[j][1]
            tree[a].append(b)
            tree[b].append(a)
            
        cnt = []  
        
        for j in range(1,n) :
            if not visited[j] :
                # print(f"{i} bfs j :", j)
                cnt.append(bfs(j,1))
                
            if len(cnt) == 2:
                res.append(abs(cnt[0]-cnt[1]))
        
    return (min(res))