#간단한 다익스트라 알고리즘 O(V^2)

import sys
imput = sys.stdin.readline
INF = int(1e9)

n,m = map(int,imput().split())
#n = # of node , m = # of edge
start = int(imput())
#시작 노드 입력
graph = [[] for i in range(n+1)]
#노드에 연결되어 있는 노드 정보를 담을 리스트
visited = [False] *  (n+1)
distance = [INF] * (n+1)

#간선에 대한 정보 입력받기
for _ in range(m):
    a,b,c = map(int,imput().split())
    # a -> b 까지 비용 c
    graph[a].append((b,c))

#방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 번호 반환
def get_smallest_node() :
    min_value = INF
    index = 0 #최단 거리가 가장 짧은 노드인덱스
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i] :
            min_value = distance[i]
            index = i
    return index

def dijkstra(start) :
    distance[start] = 0
    visited[start] = True
    #나랑 연결되어 있는 애들 확인 + 초기값 셋팅
    for j in graph[start]:
        distance[j[0]] = j[1]

    #현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True

        #현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]

            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF : 
        print(-1)
    else :
        print(distance[i])