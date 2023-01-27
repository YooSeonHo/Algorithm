import sys
imput = sys.stdin.readline

def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)

    if a < b:
        parent[b] = a
    else :
        parent[a] = b


n,m = map(int,imput().split())
parent = [0] * (n+1)

for i in range(1,n+1):
    parent[i] = i

edges = []
res = 0
#res도 필요!

for _ in range(m):
    a,b,c = map(int,imput().split())
    edges.append((c,a,b))

edges.sort()

addEdges = ()
for edge in edges:
    cost,a,b = edge
    if find(parent,a) != find(parent,b) :
        union(parent,a,b)
        addEdges = (cost,a,b)
        res += cost

res -= addEdges[0]

print(res)
#사이클이 만들어지지 않는 간선 중 마지막으로 붙을 간선은 뺴야함!
