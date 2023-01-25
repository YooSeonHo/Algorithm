#위상 정렬 -> 방향 그래프의 모든 노드들이 방향성에 거스르지 않도록 순서대로 나열하는 것
from collections import deque

v,e = map(int,input().split())
#진입 차수(노드로 진입 가능한 간선 수)!!! 모두 0으로 초기화
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]

for _ in range(e):
    a,b = map(int,input().split())
    # a -> b 이동 가능
    graph[a].append(b)
    indegree[b] +=1

def topology_sort() :
    res = []
    q = deque([])

    #처음 시작할 때 진입 차수가 0인 노드 큐에 삽입
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        res.append(now)

        #now와 연결된 노드들의 진입 차수 1 빼기
        for i in graph[now] :
            indegree[i] -= 1

            #진입 차수가 0이 되면 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    for i in res:
        print(i,end =' ')

topology_sort()