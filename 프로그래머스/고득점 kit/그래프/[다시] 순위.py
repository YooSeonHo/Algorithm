def solution(n, results):
    graph = [[0] * (n+1) for _ in range(n+1)]

    for r in results :
        a,b = r
        graph[a][b] = 1
        graph[b][a] = -1
    
    for i in range(1,n+1) :
        graph[i][i] = 2

    for k in range(1,n+1):
        for i in range(1,n+1) :
            for j in range(1,n+1) :
                if graph[i][j] != 0 :
                    continue
                if graph[i][k] == 1 and graph[k][j] == 1 :
                    graph[i][j] = 1
                    continue
                elif graph[i][k] == -1 and graph[k][j] == -1 :
                    graph[i][j] = -1
                    
    res = 0
    
    for g in graph[1:] :
        flag = False
        for v in g[1:]:
            if v == 0 :
                flag = True
                break
        if not flag :
            res += 1
            
    return res
            
    
