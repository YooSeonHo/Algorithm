from collections import deque

com = int(input())
con = int(input())
graph = [[] for _ in range(com+1)]
visited = [False] * (com+1)
for _ in range(con):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    q = deque([])
    q.append(1)
    visited[1] = True
    res = 0
    while q :
        v = q.popleft()

        for i in graph[v] :
            if not visited[i] :
                q.append(i)
                visited[i] = True
                res +=1

    return res

print(bfs())
