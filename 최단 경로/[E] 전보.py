import sys
import heapq
imput = sys.stdin.readline
INF = int(1e9)

n,m,c = map(int,imput().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b,x = map(int,imput().split())
    graph[a].append((b,x))

def dijkstra(start):
    q = []
    heapq.heappush(q,[start,0])
    distance[start] = 0

    while q:
        now,dist = heapq.heappop(q)
        if distance[now] < dist :
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,[i[0],cost])

dijkstra(c)

cnt = 0
time = 0
ans = 0

for i in distance:
    if i != INF and i != 0 :
        cnt+=1
        ans = max(ans,i)

print(cnt, ans)