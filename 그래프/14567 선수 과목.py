from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
q = deque([])
classes = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

res = []
for i in range(m):
    a,b = map(int,input().split())
    classes[a].append(b)
    indegree[b] += 1

for i in range(1,n+1) :
    if indegree[i] == 0 :
        q.append((i,1))


while q:
    v, s = q.popleft()
    res.append([v,s])

    for g in classes[v] :
        indegree[g] -= 1
        if indegree[g] == 0 :
            q.append([g,s+1])


res.sort(key=lambda x: x[0])

for i in res :
    print(i[1],end=' ')