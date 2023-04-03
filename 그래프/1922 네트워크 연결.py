import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x :
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b :
        parent[b] = a
    else :
        parent[a] = b

n = int(input())
m = int(input())

edges = []
parent = [i for i in range(n+1)]
for _ in range(m):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()
res = 0

for e in edges :
    cost,a,b = e

    if find_parent(parent,a) != find_parent(parent,b) :
        union_parent(parent,a,b)
        res += cost

print(res)