def solution(m, n, puddles):
    # 문제 = 최단 경로의 개수
    arr = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1,m+1) :
        if [i,1] not in puddles :
            arr[1][i] = 1
        else :
            break
    for i in range(1,n+1) :
        if [1,i] not in puddles :
            arr[i][1] = 1
        else :
            break
        
    for i in range(2,n+1) :
        for j in range(2,m+1) :
            if [j,i] in puddles :
                arr[i][j] = 0
            else :
                arr[i][j] = (arr[i-1][j] + arr[i][j-1]) 
    return (arr[n][m] % 1000000007)
        