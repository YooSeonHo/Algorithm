# import sys
# import heapq
# imput = sys.stdin.readline
# INF = int(1e9)

# n,m = map(int,imput().split())
# graph = [[]for _ in range(n+1)]
# distance = [INF] * (n+1)

# for i in range(m):
#     a,b = map(int,imput().split())
#     graph[a].append(b)
#     graph[b].append(a)

# x,k = map(int,imput().split())

# def dijkstra(start):
#     q =[]
#     heapq.heappush(q,(0,start))

#     while q:
#         dist,now = heapq.heappop(q)

#         if distance[now] < dist:
#             continue
        
#         for i in graph[now]:
#             cost = dist + 1
#             if cost < distance[i]:
#                 distance[i] = cost
#                 heapq.heappush(q,[cost,i])

# # 1-> k + k -> x 다익스트라 두번 ?
# dijkstra(1)
# cnt = distance[k]

# distance = [INF] * (n+1)
# dijkstra(k)
# cnt += distance[x]

# if cnt >= INF :
#     print(-1)
# else:
#     print(cnt)

#다익스트라를 두번 써서 푸는 문제라고 생각했는데 모든 노드에서 모든 노드에 대한 최단 경로인
#플로이드 워셜을 쓰면 되는거였네 선호야ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ 바보니

INF = int(1e9)
n,m = map(int,input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0

for i in range(m):
    a,b = list(map(int,input().split()))
    graph[a][b] = 1
    graph[b][a] = 1

x,k = map(int,input().split())

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

if graph[1][k] + graph[k][x] >= INF:
    print(-1)
else :
    print(graph[1][k] + graph[k][x])