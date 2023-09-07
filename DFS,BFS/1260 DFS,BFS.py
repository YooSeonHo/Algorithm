from collections import deque

n,m,v = list(map(int,input().split()))
graph = [[] for _ in range(n+1)]


for _ in range(m):
    a,b = list(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()

visited = [False] * (n+1)

def dfs(v,visited) :
    print(v,end=' ')
    visited[v] = True

    for g in graph[v]:
        if not visited[g] :
            dfs(g,visited) 

def bfs(v) :
    visited = [False] * (n+1)
    visited[v] = True
    q = deque([v])

    while q:
        vertext = q.popleft()
        print(vertext,end=' ')

        for g in graph[vertext] :
            if not visited[g] :
                q.append(g)
                visited[g] = True

dfs(v,visited)
print()
bfs(v)