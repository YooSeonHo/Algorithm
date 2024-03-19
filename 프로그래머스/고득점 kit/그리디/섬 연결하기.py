def solution(n, costs):
    
    def find_parent(x) :
        if parent[x] != x :
            parent[x] = find_parent(parent[x])
            
        return parent[x]
    
    def union(a,b) :
        a = find_parent(a)
        b = find_parent(b)
        
        if a > b :
            parent[a] = b
        else :
            parent[b] = a
          
    parent = [i for i in range(n)]
    edges = []
    
    for c in costs :
        edges.append(c[::-1])
    
    edges.sort()
    res = 0
    
    for e in edges :
        cost,a,b = e
        if find_parent(a) != find_parent(b) :
            union(a,b)
            res += cost
            
    return res