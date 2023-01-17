#개선된 다익스트라 알고리즘 O(ElovV)

import heapq
import sys
imput = sys.stdin.readline
INF = int(1e9)

n,m = map(int,imput().split())
start = int(imput())
graph = [[]for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,imput().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,[0,start])
    # 시작 노드로 가기 위한 최단 경로 0 으로 설정해서 q에 삽입
    distance[start] = 0

    while q:
        dist,now = heapq.heappop(q)
        #현재 노드가 이미 처리된 적 있다면 무시
        if distance[now] < dist :
            continue
        
        #현재 노드와 연결된 다른 인접 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] =  cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF :
        print(-1)
    else :
        print(distance[i])

        