from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
com = [i for i in range(1,n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)

def bfs(v):
    visited = [False] * (n+1)
    q = deque([])
    q.append(v)
    visited[v] = True

    res = 1
    while q:
        c = q.popleft()

        for i in graph[c] :
            if not visited[i] : 
                q.append(i)
                res += 1
                visited[i] = True

    return res

ans = []
for i in range(1,n+1):
    ans.append(bfs(i))


res = []
for i in range(len(ans)) :
    if ans[i] == max(ans) :
        res.append(i+1)


print(*res)