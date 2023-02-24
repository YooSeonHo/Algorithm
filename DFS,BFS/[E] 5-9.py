from collections import deque

def bfs(graph,start,visited):

    q = deque([start])
    visited[start] = True


    while q:
        v = q.popleft()
        print(v,end=' ')

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

#넣고 방문처리!!!!! 까묵지 말장 ㅋ

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

bfs(graph,1,visited)