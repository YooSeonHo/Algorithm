import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
n,m,x = map(int,input().split())
graph = [[]for _ in range(n+1)]
reverse_graph = [[]for _ in range(n+1)]


for _ in range(m):
    a,b,t = map(int,input().split())
    graph[a].append((b,t))
    reverse_graph[b].append((a,t))

def dijkstra(g,start) :
    times = [INF] * (n+1)
    q = []
    times[start] = 0
    heapq.heappush(q,[start,0])

    while q :
        now,time = heapq.heappop(q)

        if time > times[now] :
            continue
        for v in g[now]:
            t = v[1] + time
            if times[v[0]] > t :
                times[v[0]] = t
                heapq.heappush(q,[v[0],t])

    # res.append(times)
    return times


ans = dijkstra(graph,x)
ans_re = dijkstra(reverse_graph,x)
for i in range(1,len(ans)):
    ans[i] += ans_re[i]

ans[0] = 0
print(max(ans))

#step 1. x에서 다익스트라 -> x에서 돌아가는 모든 노드에 대한 최솟값을 구할 수 ㅇ
#step 2. 그래프의 방향을 반대로 바꿈 => x에서 다익스트라 -> x로 들어가는 모든 노드에 대한 최솟값을 구할 수 ㅇ
#와 이거 진짜 미쳤다..


# ans = []
# res = []
# for i in range(1,n+1):
#     ans.append(dijkstra(i))
# for i in range(len(ans)):
#     if i == x :
#         continue
#     res.append(ans[i][x] + ans[x-1][i+1])

# print(max(res))


#다익스트라 두번하는게 아니라 x의 행을 보면 다시 돌아가는 최소 거리가 나와있다!!!!!!!!!!!!!!!!!!!!!!!
