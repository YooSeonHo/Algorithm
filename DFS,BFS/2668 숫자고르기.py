import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
res = []
for i in range(1,n+1):
    num = int(input())
    if num == i :
        res.append(i)
    else:
        graph[i].append(num)
    
visited = [False] * (n+1)

def dfs(start,v):
    global res
    if visited[v] :
        if start == v :
            res += tmp
        #시작점에서 사이클이 생성됐다면!
        elif v in tmp :
            res += tmp[tmp.index(v):]
        #시작점과 다른 곳에서 사이클이 생성 됐으면!
        return

    tmp.append(v)
    visited[v] = True
    for i in graph[v]:
        dfs(start,i)

for i in range(1,n+1):
    tmp = []
    if not visited[i]:
        dfs(i,i)

res.sort()
print(len(res),*res,sep='\n')
