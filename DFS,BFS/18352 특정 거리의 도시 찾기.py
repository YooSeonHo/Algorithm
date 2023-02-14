from collections import deque
import sys
input = sys.stdin.readline

n,m,k,x = map(int,input().split())
city = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = [0] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    city[a].append(b)

q = deque([(x,-1)])
visited[x] = True

while q:
    v,count = q.popleft()
    cnt[v] = count +1

    for i in city[v]:
        if not visited[i] :
            q.append((i,cnt[v]))
            visited[i] = True
flag = False
for i in range(1,n+1) :
    if cnt[i] == k :
        print(i)
        flag = True

if not flag :
    print(-1)



