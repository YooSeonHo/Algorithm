
import heapq

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for i in range(m):
    a,b = list(map(int,input().split()))
    graph[a].append(b)
    indegree[b] += 1

def topology_sort() :
    res = []
    q = []

    for i in range(1,n+1) :
        if indegree[i] == 0:
            heapq.heappush(q,i)
    
    while q:
        index = heapq.heappop(q)
        res.append(index)

        for i in graph[index]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q,i)

        

    for i in range(n):
        print(res[i],end=' ')

topology_sort()
