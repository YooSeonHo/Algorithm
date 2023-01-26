def find_team(parent,x) : 
    if parent[x] != x:
        parent[x] = find_team(parent,parent[x])
    return parent[x]

def union_team(parent,a,b):
    a = find_team(parent,a)
    b = find_team(parent,b)
    #여기서 find 안하고 걍 parent[a], parent[b] 비교하면 안되낭? -> 도전해보기
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

n,m = map(int,input().split())
parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i


for _ in range(m):
    op,a,b = map(int,input().split())

    if op == 0 :
        union_team(parent,a,b)
    else :
        aTeam = find_team(parent,a)
        bTeam = find_team(parent,b)

        if aTeam == bTeam :
            print('YES')
        else :
            print('NO')




