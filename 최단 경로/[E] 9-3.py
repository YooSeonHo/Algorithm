#플로이드 워셜 알고리즘 O(N^3)

INF = int(1e9)
n = int(input())
m = int(input())
#n = # of node, m = # of edge

#2차원 리스트로 그래프를 만들고 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

#자기 자신 0으로 초기화
for i in range(1,n+1):
    graph[i][i] = 0

#간선 정보 입력 받아 그 값으로 초기화
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c
    #단방향이니까 이것만 ㅋ 양방향이면 반대도 해줘야대잉

#점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF :
            print(-1)
        else :
            print(graph[a][b], end=' ')

    print()

